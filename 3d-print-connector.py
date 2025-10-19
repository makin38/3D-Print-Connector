bl_info = {
    "name": "3D Print Connector",
    "author": "Mustafa Akin",
    "version": (1, 0, 0),
    "blender": (3, 0, 0),
    "location": "View3D > Sidebar > 3D Print Connector",
    "description": "İki objeyi birleştirmek için tenon ve mortise bağlantılar oluşturur",
    "category": "Object",
}

import bpy
from bpy.types import Operator, Panel, PropertyGroup
from bpy.props import FloatProperty, StringProperty
from bpy.app.translations import pgettext as _

class ConnectorProperties(PropertyGroup):
    object1: StringProperty(default="")
    object2: StringProperty(default="")
    connector_obj: StringProperty(default="")
    
    tolerance_x: FloatProperty(
        name="X Axis Tolerance (mm)",
        description="X axis mortise gap - ALWAYS in millimeters",
        default=0.2,
        min=0.0,
        max=5.0,
        precision=2
    )
    
    tolerance_y: FloatProperty(
        name="Y Axis Tolerance (mm)",
        description="Y axis mortise gap - ALWAYS in millimeters",
        default=0.2,
        min=0.0,
        max=5.0,
        precision=2
    )
    
    tolerance_z: FloatProperty(
        name="Z Axis Tolerance (mm)",
        description="Z axis mortise gap - ALWAYS in millimeters",
        default=0.5,
        min=0.0,
        max=5.0,
        precision=2
    )
    
    chamfer_size: FloatProperty(
        name="Chamfer Size (mm)",
        description="Chamfer size for connector edges - ALWAYS in millimeters",
        default=0.5,
        min=0.0,
        max=20.0,
        precision=2
    )

class OBJECT_OT_select_object_1(Operator):
    """First object selection"""
    bl_idname = "object.select_connector_object_1"
    bl_label = "Select Object 1"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        obj = context.active_object
        if not obj or obj.type != 'MESH':
            self.report({'ERROR'}, _("Please select a mesh object"))
            return {'CANCELLED'}
        
        props = context.scene.connector_props
        props.object1 = obj.name
        
        self.report({'INFO'}, _("Object 1 selected:") + f" {obj.name}")
        return {'FINISHED'}

class OBJECT_OT_select_object_2(Operator):
    """Second object selection"""
    bl_idname = "object.select_connector_object_2"
    bl_label = "Select Object 2"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        obj = context.active_object
        if not obj or obj.type != 'MESH':
            self.report({'ERROR'}, _("Please select a mesh object"))
            return {'CANCELLED'}
        
        props = context.scene.connector_props
        props.object2 = obj.name
        
        self.report({'INFO'}, _("Object 2 selected:") + f" {obj.name}")
        return {'FINISHED'}

class OBJECT_OT_select_connector(Operator):
    """Connector piece selection"""
    bl_idname = "object.select_connector_piece"
    bl_label = "Select Connector Piece"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        obj = context.active_object
        if not obj or obj.type != 'MESH':
            self.report({'ERROR'}, _("Please select a mesh object"))
            return {'CANCELLED'}
        
        props = context.scene.connector_props
        props.connector_obj = obj.name
        
        self.report({'INFO'}, _("Connector selected:") + f" {obj.name}")
        return {'FINISHED'}

class OBJECT_OT_create_mortises(Operator):
    """Create mortises in both objects"""
    bl_idname = "object.create_mortises"
    bl_label = "Create Mortises"
    bl_options = {'REGISTER', 'UNDO'}
    
    def get_unit_scale_to_mm(self):
        """Blender birim sistemini mm'ye çevirme faktörünü hesapla
        
        Blender'da iç koordinatlar her zaman METRE cinsindendir.
        Unit settings sadece display ve input/output için kullanılır.
        Bu yüzden 1 Blender Unit = 1 metre olarak işlem yaparız.
        """
        scene = bpy.context.scene
        unit_settings = scene.unit_settings
        
        # Unit scale faktörü
        scale = unit_settings.scale_length
        
        # Blender'ın internal koordinatları METRE cinsindendir
        # 1 Blender Unit = 1 metre * scale_length
        # 1 metre = 1000 mm
        mm_per_unit = 1000.0 * scale
        
        return mm_per_unit
    
    def mm_to_blender_units(self, mm_value):
        """Milimetre değerini Blender birimlerine çevir"""
        mm_per_unit = self.get_unit_scale_to_mm()
        return mm_value / mm_per_unit
    
    def execute(self, context):
        props = context.scene.connector_props
        
        # Kontroller
        if not props.object1:
            self.report({'ERROR'}, _("Object 1 not selected"))
            return {'CANCELLED'}
        
        if not props.object2:
            self.report({'ERROR'}, _("Object 2 not selected"))
            return {'CANCELLED'}
        
        if not props.connector_obj:
            self.report({'ERROR'}, _("Connector piece not selected"))
            return {'CANCELLED'}
        
        obj1 = bpy.data.objects.get(props.object1)
        obj2 = bpy.data.objects.get(props.object2)
        connector = bpy.data.objects.get(props.connector_obj)
        
        if not obj1:
            self.report({'ERROR'}, _("Object 1 not found:") + f" {props.object1}")
            return {'CANCELLED'}
        
        if not obj2:
            self.report({'ERROR'}, _("Object 2 not found:") + f" {props.object2}")
            return {'CANCELLED'}
        
        if not connector:
            self.report({'ERROR'}, _("Connector not found:") + f" {props.connector_obj}")
            return {'CANCELLED'}
        
        # Object mode'da olduğundan emin ol
        if context.mode != 'OBJECT':
            bpy.ops.object.mode_set(mode='OBJECT')
        
        # ÖNEMLİ: Connector'ın scale'ini apply et (1,1,1 yap)
        # Bu, pah işleminin uniform olması için kritik!
        bpy.context.view_layer.objects.active = connector
        bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
        print(f"Connector scale applied: {connector.scale}")
        
        # Toleransı Blender birimlerine çevir (mm'den)
        tolerance_x_bu = self.mm_to_blender_units(props.tolerance_x)
        tolerance_y_bu = self.mm_to_blender_units(props.tolerance_y)
        tolerance_z_bu = self.mm_to_blender_units(props.tolerance_z)
        
        # Debug bilgisi
        mm_per_bu = self.get_unit_scale_to_mm()
        print(f"\n=== BİRİM SİSTEMİ BİLGİLERİ ===")
        print(f"Blender Unit Settings: {context.scene.unit_settings.length_unit}")
        print(f"Scale: {context.scene.unit_settings.scale_length}")
        print(f"1 Blender Unit = {mm_per_bu:.4f} mm")
        print(f"X Tolerans: {props.tolerance_x} mm = {tolerance_x_bu:.6f} BU")
        print(f"Y Tolerans: {props.tolerance_y} mm = {tolerance_y_bu:.6f} BU")
        print(f"Z Tolerans: {props.tolerance_z} mm = {tolerance_z_bu:.6f} BU")
        print(f"Pah: {props.chamfer_size} mm = {self.mm_to_blender_units(props.chamfer_size):.6f} BU")
        print(f"================================\n")
        
        # Connector'ın kopyalarını oluştur (toleranslı) - PAH OLMADAN
        cutter1 = self.create_cutter_copy(connector, tolerance_x_bu, tolerance_y_bu, tolerance_z_bu, "Cutter_1")
        cutter2 = self.create_cutter_copy(connector, tolerance_x_bu, tolerance_y_bu, tolerance_z_bu, "Cutter_2")
        
        # Object 1'e boolean uygula
        success1 = self.apply_boolean(obj1, cutter1)
        
        # Object 2'ye boolean uygula
        success2 = self.apply_boolean(obj2, cutter2)
        
        # EN SON: Orijinal connector'a pah uygula (sadece connector'da pah olsun)
        if props.chamfer_size > 0:
            chamfer_bu = self.mm_to_blender_units(props.chamfer_size)
            self.apply_chamfer(connector, chamfer_bu)
        
        if success1 and success2:
            mm_per_unit = self.get_unit_scale_to_mm()
            self.report({'INFO'}, _("Mortises created!") + f" (1 BU = {mm_per_unit:.3f} mm)")
            # Connector'ı görünür tut
            connector.hide_set(False)
        else:
            self.report({'WARNING'}, _("Some boolean operations failed"))
        
        return {'FINISHED'}
    
    def create_cutter_copy(self, original, tolerance_x_bu, tolerance_y_bu, tolerance_z_bu, name):
        """Connector'ın toleranslı kopyasını oluştur
        
        tolerance_x_bu: X ekseni toleransı (Blender Unit)
        tolerance_y_bu: Y ekseni toleransı (Blender Unit)
        tolerance_z_bu: Z ekseni toleransı (Blender Unit)
        """
        # Kopyala
        cutter = original.copy()
        cutter.data = original.data.copy()
        cutter.name = name
        bpy.context.collection.objects.link(cutter)
        
        # Tolerans ekle - Scale yöntemi
        if tolerance_x_bu > 0 or tolerance_y_bu > 0 or tolerance_z_bu > 0:
            # Objeyi aktif yap
            bpy.context.view_layer.objects.active = original
            
            # Mesh'in dünya koordinatlarındaki boyutlarını al
            if original.type == 'MESH':
                # Transform matrix uygulanmış vertex pozisyonları
                verts_world = [original.matrix_world @ v.co for v in original.data.vertices]
                
                if verts_world:
                    # Boyutları hesapla (metre cinsinden, çünkü internal coordinates metre)
                    min_x = min(v.x for v in verts_world)
                    max_x = max(v.x for v in verts_world)
                    min_y = min(v.y for v in verts_world)
                    max_y = max(v.y for v in verts_world)
                    min_z = min(v.z for v in verts_world)
                    max_z = max(v.z for v in verts_world)
                    
                    # Boyutlar metre cinsinden (Blender internal coordinates)
                    current_x_m = max_x - min_x
                    current_y_m = max_y - min_y
                    current_z_m = max_z - min_z
                    
                    # Metre'yi mm'ye çevir
                    current_x_mm = current_x_m * 1000
                    current_y_mm = current_y_m * 1000
                    current_z_mm = current_z_m * 1000
                    
                    # mm'yi Blender Unit'e çevir
                    mm_per_bu = self.get_unit_scale_to_mm()
                    current_x_bu = current_x_mm / mm_per_bu
                    current_y_bu = current_y_mm / mm_per_bu
                    current_z_bu = current_z_mm / mm_per_bu
                    
                    # Debug
                    print(f"Connector dimensions in BU: X={current_x_bu:.4f}, Y={current_y_bu:.4f}, Z={current_z_bu:.4f}")
                    print(f"X Tolerance: {tolerance_x_bu:.4f} BU")
                    print(f"Y Tolerance: {tolerance_y_bu:.4f} BU")
                    print(f"Z Tolerance: {tolerance_z_bu:.4f} BU")
                    print(f"1 BU = {mm_per_bu:.4f} mm")
                    
                    # Scale faktörlerini hesapla (her eksende 2x tolerans ekliyoruz - her iki taraf için)
                    scale_x = (current_x_bu + tolerance_x_bu * 2) / current_x_bu if current_x_bu > 0 else 1.0
                    scale_y = (current_y_bu + tolerance_y_bu * 2) / current_y_bu if current_y_bu > 0 else 1.0
                    scale_z = (current_z_bu + tolerance_z_bu * 2) / current_z_bu if current_z_bu > 0 else 1.0
                    
                    print(f"Scale factors: X={scale_x:.4f}, Y={scale_y:.4f}, Z={scale_z:.4f}")
                    
                    # Yeni scale'i uygula
                    cutter.scale = (
                        original.scale[0] * scale_x,
                        original.scale[1] * scale_y,
                        original.scale[2] * scale_z
                    )
        
        return cutter
    
    def apply_chamfer(self, obj, chamfer_size):
        """Connector'ın tüm kenarlarına gerçek 45 derece uniform pah uygula"""
        try:
            # Objeyi aktif yap
            bpy.context.view_layer.objects.active = obj
            
            # ÖNCE SCALE'İ APPLY ET - Bu çok önemli!
            # Scale farklıysa bevel uniform olmaz
            bpy.ops.object.mode_set(mode='OBJECT')
            bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
            
            # Edit mode'a geç
            bpy.ops.object.mode_set(mode='EDIT')
            
            # Tüm kenarları seç
            bpy.ops.mesh.select_all(action='SELECT')
            bpy.ops.mesh.select_mode(type='EDGE')
            
            # Bevel (pah) uygula - Blender 4.x uyumlu basit ayarlar
            # WIDTH modu en uniform sonucu verir
            bpy.ops.mesh.bevel(
                offset=chamfer_size,
                offset_type='WIDTH',  # WIDTH en tutarlı sonucu verir
                segments=3,  # 45 derece pah için segments=3
                profile=0.5,  # 0.5 = 45 derece
                affect='EDGES',
                clamp_overlap=True
            )
            
            # Object mode'a dön
            bpy.ops.object.mode_set(mode='OBJECT')
            
            print(f"Pah uygulandı: {chamfer_size:.6f} BU genişliğinde")
            return True
        except Exception as e:
            print(f"Pah uygulama hatası: {e}")
            import traceback
            traceback.print_exc()
            bpy.ops.object.mode_set(mode='OBJECT')
            return False
    
    def apply_boolean(self, target_obj, cutter_obj):
        """Boolean modifier uygula"""
        try:
            # Boolean modifier ekle
            mod = target_obj.modifiers.new(name="Mortise_Cut", type='BOOLEAN')
            mod.operation = 'DIFFERENCE'
            mod.object = cutter_obj
            
            # Modifier'ı uygula
            context = bpy.context
            context.view_layer.objects.active = target_obj
            bpy.ops.object.modifier_apply(modifier=mod.name)
            
            # Kesiciyi sil
            bpy.data.objects.remove(cutter_obj, do_unlink=True)
            
            return True
        except Exception as e:
            print(f"Boolean hatası: {e}")
            return False

class OBJECT_OT_reset_selection(Operator):
    """Reset all selections"""
    bl_idname = "object.reset_connector_selection"
    bl_label = "Reset Selection"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        props = context.scene.connector_props
        props.object1 = ""
        props.object2 = ""
        props.connector_obj = ""
        
        self.report({'INFO'}, _("Selections reset"))
        return {'FINISHED'}

class VIEW3D_PT_connector_panel(Panel):
    """3D Print Connector Panel"""
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = '3D Print Connector'
    bl_label = "Tenon-Mortise Connector"
    
    def draw(self, context):
        layout = self.layout
        props = context.scene.connector_props
        
        # Talimatlar
        box = layout.box()
        box.label(text=_("Usage:"), icon='INFO')
        box.label(text=_("1. Select first object → Select Object 1"))
        box.label(text=_("2. Select second object → Select Object 2"))
        box.label(text=_("3. Select connector piece → Select Connector"))
        box.label(text=_("4. Set tolerance for each axis (mm)"))
        box.label(text=_("   • Adjust according to connector orientation"))
        box.label(text=_("   • Give more to depth axis"))
        box.label(text=_("5. Click Create Mortises"))
        
        layout.separator()
        
        # Obje seçimi
        box = layout.box()
        box.label(text=_("1. Select Objects:"), icon='OBJECT_DATA')
        
        row = box.row(align=True)
        row.operator("object.select_connector_object_1", text="Select Object 1")
        if props.object1:
            row.label(text="✓", icon='CHECKMARK')
        
        if props.object1:
            box.label(text=f"   → {props.object1}", icon='MESH_CUBE')
        
        row = box.row(align=True)
        row.operator("object.select_connector_object_2", text="Select Object 2")
        if props.object2:
            row.label(text="✓", icon='CHECKMARK')
        
        if props.object2:
            box.label(text=f"   → {props.object2}", icon='MESH_CUBE')
        
        row = box.row(align=True)
        row.operator("object.select_connector_piece", text="Select Connector Piece")
        if props.connector_obj:
            row.label(text="✓", icon='CHECKMARK')
        
        if props.connector_obj:
            box.label(text=f"   → {props.connector_obj}", icon='MESH_DATA')
        
        # Ayarlar
        layout.separator()
        box = layout.box()
        box.label(text=_("2. Settings:"), icon='PREFERENCES')
        
        # Mevcut birim sistemini göster
        unit_settings = context.scene.unit_settings
        scale = unit_settings.scale_length
        length_unit = unit_settings.length_unit
        
        # 1 BU = ? mm hesapla
        mm_per_bu = 1000.0 * scale
        
        # Birim bilgisi - daha detaylı
        info_box = box.box()
        info_box.label(text=_("Blender Unit:") + f" {length_unit}", icon='INFO')
        info_box.label(text=_("Scale:") + f" {scale:.3f}", icon='BLANK1')
        info_box.label(text=f"1 BU = {mm_per_bu:.3f} mm", icon='BLANK1')
        
        # Tolerans ve pah her zaman MM cinsinden
        box.separator()
        box.label(text=_("All values are in MM:"), icon='CHECKMARK')
        
        # X ekseni toleransı
        box.prop(props, "tolerance_x")
        box.label(text=_("(X axis gap)"), icon='BLANK1')
        
        # Y ekseni toleransı
        box.prop(props, "tolerance_y")
        box.label(text=_("(Y axis gap)"), icon='BLANK1')
        
        # Z ekseni toleransı
        box.prop(props, "tolerance_z")
        box.label(text=_("(Z axis gap)"), icon='BLANK1')
        
        box.separator()
        box.label(text=_("💡 Tip: Give more tolerance to"), icon='INFO')
        box.label(text=_("   depth axis (e.g., 0.5mm)"), icon='BLANK1')
        box.label(text=_("   Less to side axes (e.g., 0.2mm)"), icon='BLANK1')
        
        # Pah
        box.separator()
        box.prop(props, "chamfer_size")
        box.label(text=_("(Only connector edges)"), icon='BLANK1')
        
        # Oluştur
        layout.separator()
        box = layout.box()
        box.label(text=_("3. Create Mortises:"), icon='MOD_BOOLEAN')
        
        # Tüm seçimler yapıldıysa düğmeyi etkinleştir
        if props.object1 and props.object2 and props.connector_obj:
            box.operator("object.create_mortises", text=_("Create Mortises"), icon='PLAY')
        else:
            row = box.row()
            row.enabled = False
            row.operator("object.create_mortises", text=_("Create Mortises (Select first)"), icon='ERROR')
        
        # Reset düğmesi
        layout.separator()
        layout.operator("object.reset_connector_selection", text="Reset Selection", icon='FILE_REFRESH')

classes = (
    ConnectorProperties,
    OBJECT_OT_select_object_1,
    OBJECT_OT_select_object_2,
    OBJECT_OT_select_connector,
    OBJECT_OT_create_mortises,
    OBJECT_OT_reset_selection,
    VIEW3D_PT_connector_panel,
)

# Çeviri sözlüğü - Türkçe
translations_dict = {
    "tr_TR": {
        ("*", "3D Print Tenon-Mortise Connector"): "3D Baskı Tenon-Mortise Konnektörü",
        ("*", "Create Mortises"): "Girinti Oluştur",
        ("*", "Select Object 1"): "Obje 1'i Seç",
        ("*", "Select Object 2"): "Obje 2'yi Seç",
        ("*", "Select Connector Piece"): "Konnektör Parçasını Seç",
        ("*", "Reset Selection"): "Seçimi Sıfırla",
        ("*", "Tenon-Mortise Connector"): "Tenon-Mortise Konnektör",
        
        # Operator açıklamaları
        ("*", "First object selection"): "Birinci objeyi seç",
        ("*", "Second object selection"): "İkinci objeyi seç",
        ("*", "Connector piece selection"): "Bağlantı parçasını seç",
        ("*", "Create mortises in both objects"): "Her iki objede girinti oluştur",
        ("*", "Reset all selections"): "Tüm seçimleri sıfırla",
        
        # Property açıklamaları
        ("*", "X Axis Tolerance (mm)"): "X Ekseni Tolerans (mm)",
        ("*", "X axis mortise gap - ALWAYS in millimeters"): "X ekseninde girinti boşluğu - HER ZAMAN milimetre cinsinden",
        ("*", "Y Axis Tolerance (mm)"): "Y Ekseni Tolerans (mm)",
        ("*", "Y axis mortise gap - ALWAYS in millimeters"): "Y ekseninde girinti boşluğu - HER ZAMAN milimetre cinsinden",
        ("*", "Z Axis Tolerance (mm)"): "Z Ekseni Tolerans (mm)",
        ("*", "Z axis mortise gap - ALWAYS in millimeters"): "Z ekseninde girinti boşluğu - HER ZAMAN milimetre cinsinden",
        ("*", "Chamfer Size (mm)"): "Pah Boyutu (mm)",
        ("*", "Chamfer size for connector edges - ALWAYS in millimeters"): "Connector'ın kenarlarına uygulanacak pah boyutu - HER ZAMAN milimetre cinsinden",
        
        # UI metinleri
        ("*", "Usage:"): "Kullanım:",
        ("*", "1. Select first object → Select Object 1"): "1. İlk objeyi seç → Obje 1'i Seç",
        ("*", "2. Select second object → Select Object 2"): "2. İkinci objeyi seç → Obje 2'yi Seç",
        ("*", "3. Select connector piece → Select Connector"): "3. Bağlantı parçasını seç → Konnektör'ü Seç",
        ("*", "4. Set tolerance for each axis (mm)"): "4. Her eksen için tolerans ayarla (mm)",
        ("*", "   • Adjust according to connector orientation"): "   • Konnektör'ın yönüne göre ayarlayın",
        ("*", "   • Give more to depth axis"): "   • Derinlik eksenine daha fazla verin",
        ("*", "5. Click Create Mortises"): "5. Girinti Oluştur'a tıkla",
        
        ("*", "1. Select Objects:"): "1. Objeleri Seç:",
        ("*", "2. Settings:"): "2. Ayarlar:",
        ("*", "3. Create Mortises:"): "3. Girintileri Oluştur:",
        
        ("*", "Blender Unit:"): "Blender Birimi:",
        ("*", "Scale:"): "Ölçek:",
        ("*", "All values are in MM:"): "Tüm değerler MM cinsindendir:",
        
        ("*", "(X axis gap)"): "(X ekseni boşluğu)",
        ("*", "(Y axis gap)"): "(Y ekseni boşluğu)",
        ("*", "(Z axis gap)"): "(Z ekseni boşluğu)",
        
        ("*", "💡 Tip: Give more tolerance to"): "💡 İpucu: Derinlik eksenine daha",
        ("*", "   depth axis (e.g., 0.5mm)"): "   fazla tolerans verin (ör: 0.5mm)",
        ("*", "   Less to side axes (e.g., 0.2mm)"): "   Kenar eksenlerine az (ör: 0.2mm)",
        
        ("*", "(Only connector edges)"): "(Sadece konnektör kenarlarına)",
        
        ("*", "Create Mortises (Select first)"): "Girinti Oluştur (Önce seç)",
        
        # Hata mesajları
        ("*", "Please select a mesh object"): "Lütfen bir mesh objesi seçin",
        ("*", "Object 1 not selected"): "Obje 1 seçilmedi",
        ("*", "Object 2 not selected"): "Obje 2 seçilmedi",
        ("*", "Connector piece not selected"): "Konnektör parçası seçilmedi",
        ("*", "Object 1 not found:"): "Obje 1 bulunamadı:",
        ("*", "Object 2 not found:"): "Obje 2 bulunamadı:",
        ("*", "Connector not found:"): "Konnektör bulunamadı:",
        
        # Başarı mesajları
        ("*", "Object 1 selected:"): "Obje 1 seçildi:",
        ("*", "Object 2 selected:"): "Obje 2 seçildi:",
        ("*", "Connector selected:"): "Konnektör seçildi:",
        ("*", "Mortises created!"): "Girintiler oluşturuldu!",
        ("*", "Some boolean operations failed"): "Bazı boolean işlemleri başarısız oldu",
        ("*", "Selections reset"): "Seçimler sıfırlandı",
    }
}

def register():
    # Çevirileri kaydet
    bpy.app.translations.register(__name__, translations_dict)
    
    for cls in classes:
        bpy.utils.register_class(cls)
    bpy.types.Scene.connector_props = bpy.props.PointerProperty(type=ConnectorProperties)

def unregister():
    # Çevirileri kaldır
    bpy.app.translations.unregister(__name__)
    
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
    del bpy.types.Scene.connector_props

if __name__ == "__main__":
    register()