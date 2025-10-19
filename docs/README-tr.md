# 3D Print Connector - Blender Eklentisi

![Blender](https://img.shields.io/badge/Blender-3.0+-orange.svg)
![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)
![License](https://img.shields.io/badge/License-GPL--3.0-green.svg)
![Version](https://img.shields.io/badge/Version-1.3.3-brightgreen.svg)

**[English](../README.md) | [Türkçe](README-tr.md)**

**3D Print Connector**, Blender'da iki objeyi birleştirmek için profesyonel **tenon-mortise** (kırlangıç kuyruğu) bağlantılar oluşturan güçlü bir eklentidir. 3D baskı projelerinizde hassas ve güvenilir birleştirmeler yapmak için tasarlanmıştır.

## ✨ Özellikler

- 🔧 **Hassas Tenon-Mortise Bağlantıları**: İki obje arasında mükemmel oturan bağlantılar
- 📏 **Milimetre Tabanlı Tolerans Kontrolü**: X, Y, Z eksenlerinde ayrı ayrı hassas ayar
- ⚙️ **Akıllı Birim Sistemi**: Blender'ın tüm birim sistemleriyle uyumlu (mm, cm, m, inch)
- 🔄 **Otomatik Pah (Chamfer)**: Bağlantı parçalarının kenarlarında profesyonel bitirme
- 🎯 **Kullanıcı Dostu Arayüz**: Adım adım rehberli basit kullanım
- 🌍 **Çoklu Dil Desteği**: Türkçe ve İngilizce arayüz
- ⚡ **Otomatik Boolean İşlemleri**: Hızlı ve temiz kesim operasyonları

## 🎯 Kullanım Alanları

- **3D Baskı Projeleri**: Büyük parçaları küçük bölümlere ayırma
- **Modüler Tasarımlar**: Birleştirilebilir oyuncaklar ve maketler
- **Mobilya ve Dekorasyon**: Ahşap işçiliği benzeri bağlantılar
- **Mühendislik Uygulamaları**: Hassas mekanik birleştirmeler
- **Prototipleme**: Hızlı montaj-demontaj gerektiren tasarımlar

## 📦 Kurulum

### Otomatik Kurulum (Önerilen)

1. [Son sürümü indirin](https://github.com/makin38/3D-Print-Connector/blob/master/3d-print-connector.py) (`.py` dosyası)
2. Blender'ı açın
3. `Edit > Preferences > Add-ons` menüsüne gidin
4. `Install...` butonuna tıklayın
5. İndirdiğiniz `.py` dosyasını seçin
6. "3D Print Connector" eklentisini etkinleştirin ✅

### Manuel Kurulum

```bash
# Blender scripts klasörünü bulun
~/AppData/Roaming/Blender/3.x/scripts/addons/  # Windows
~/Library/Application Support/Blender/3.x/scripts/addons/  # macOS
~/.config/blender/3.x/scripts/addons/  # Linux

# e3d-print-connector.py dosyasını bu klasöre kopyalayın
```

## 🚀 Hızlı Başlangıç

### Adım 1: Eklentiyi Açın
Blender'da `N` tuşuna basarak yan paneli açın ve **"3D Print Connector"** sekmesini bulun.

### Adım 2: Objeleri Hazırlayın
```
Örnek Senaryo:
• Ana Parça (büyük obje) - birleştirilecek ana parça
• İkinci Parça - ana parçaya bağlanacak parça  
• Konnektör Parçası - iki parçayı birleştirecek tenon parçası
```

### Adım 3: Seçim Yapın
1. **Ana parçayı** seçin → `Select Object 1` butonuna tıklayın ✅
2. **İkinci parçayı** seçin → `Select Object 2` butonuna tıklayın ✅
3. **Konnektör parçasını** seçin → `Select Connector Piece` butonuna tıklayın ✅

### Adım 4: Toleransları Ayarlayın
```
Önerilen Değerler:
• X Ekseni: 0.2 mm (yan tolerans)
• Y Ekseni: 0.2 mm (yan tolerans)  
• Z Ekseni: 0.5 mm (derinlik toleransı - daha gevşek)
• Pah: 0.5 mm (kenar yumuşatma)
```

### Adım 5: Oluşturun!
`Create Mortises` butonuna tıklayın ve sihri izleyin! ✨

## ⚙️ Detaylı Ayarlar

### Tolerans Kontrolü

| Eksen | Açıklama | Önerilen Değer | Kullanım |
|-------|----------|----------------|----------|
| **X** | Yan tolerans | 0.1-0.3 mm | Sıkı oturma için az |
| **Y** | Yan tolerans | 0.1-0.3 mm | Sıkı oturma için az |
| **Z** | Derinlik toleransı | 0.3-0.8 mm | Kolay takma için fazla |

### Pah (Chamfer) Ayarları

- **0.0 mm**: Pah yok (keskin kenarlar)
- **0.3-0.5 mm**: Standart pah (önerilen)
- **1.0+ mm**: Büyük pah (estetik görünüm)

### Birim Sistemi Desteği

Eklenti otomatik olarak Blender'ın birim ayarlarını algılar:

```
✅ Desteklenen Birimler:
• Milimetre (mm) - varsayılan
• Santimetre (cm)
• Metre (m)
• İnç (inch)
• Feet

💡 Tolerans değerleri her zaman MM cinsindendir!
```
## 🔧 Teknik Detaylar

### Algoritma
1. **Konnektör Analizi**: Seçilen konnektör parçasının boyutları hesaplanır
2. **Tolerans Uygulaması**: Her eksende belirtilen tolerans değerleri eklenir
3. **Boolean Operasyonu**: Hassas mortise (girinti) kesimi yapılır
4. **Pah Uygulaması**: Sadece konnektör parçasına kenar yumuşatması

### Performans
- ⚡ **Hızlı İşlem**: Saniyeler içinde tamamlanır
- 🎯 **Hassas Hesaplama**: Mikron seviyesinde doğruluk
- 💾 **Hafıza Dostu**: Büyük mesh'lerde bile verimli

### Uyumluluk
- **Blender**: 3.0+ (LTS)
- **Python**: 3.7+
- **Platform**: Windows, macOS, Linux

## 🛠️ Sorun Giderme

### Yaygın Sorunlar

#### Problem: "Boolean operation failed"
```
Çözüm:
1. Mesh'lerin manifold olduğundan emin olun
2. Objelerin scale'ini apply edin (Ctrl+A)
3. Duplicate vertex'leri temizleyin
```

#### Problem: Tolerans çok sıkı/gevşek
```
Çözüm:
1. Z eksenini (derinlik) 0.5mm yapın
2. X,Y eksenlerini 0.2mm'den başlayın
3. Test baskısı yaparak ayarlayın
```

#### Problem: Pah düzgün uygulanmıyor
```
Çözüm:
1. Konnektör objesinin scale'ini apply edin
2. Mesh'de non-manifold kenarlar olup olmadığını kontrol edin
3. Pah değerini küçültün (0.3-0.5mm)
```

### Debug Modu
Blender Console'da (`Window > Toggle System Console`) detaylı bilgileri görebilirsiniz:

```python
=== BİRİM SİSTEMİ BİLGİLERİ ===
Blender Unit Settings: MILLIMETERS
Scale: 0.001
1 Blender Unit = 1.000 mm
X Tolerans: 0.2 mm = 0.000200 BU
```

## 🤝 Katkıda Bulunma

Bu proje açık kaynaklıdır ve katkılarınızı memnuniyetle karşılıyoruz!

### Geliştirme Ortamı
```bash
git clone https://github.com/makin38/3d-print-connector.git
cd 3d-print-connector

# Blender development modunda test
blender --background --python 3d-print-connector.py
```

### Katkı Türleri
- 🐛 **Bug Raporları**: [Issues](https://github.com/makin38/3d-print-connector/issues)
- 💡 **Özellik Önerileri**: Yeni fikirlerinizi paylaşın
- 🌍 **Çeviri**: Yeni dil desteği ekleyin
- 📖 **Dokümantasyon**: README ve wiki iyileştirmeleri
- 💻 **Kod**: Pull request'ler her zaman hoş geldiniz

### Geliştirme Kuralları
1. **PEP 8** Python kod standardını takip edin
2. **Türkçe + İngilizce** yorum yazın
3. **Test edin**: Değişikliklerinizi farklı senaryolarda test edin
4. **Dokümante edin**: Yeni özellikler için README güncelleyin

## 📋 Yapılacaklar (Roadmap)

### v1.1.0 (Gelecek Sürüm)
- [ ] 🔄 **Batch İşleme**: Çoklu obje desteği
- [ ] 📐 **Özel Konnektör Şekilleri**: Yuvarlak, altıgen, custom
- [ ] 💾 **Preset Sistemi**: Tolerans ayarlarını kaydetme
- [ ] 🎨 **Material Otomasyonu**: Baskı renkleri için otomatik material atama

### v1.2.0 (Uzun Vadeli)
- [ ] 🤖 **AI Optimizasyon**: Otomatik tolerans önerisi
- [ ] 📱 **Export Optimizasyonu**: STL/3MF export ayarları
- [ ] 🔗 **Slic3r Entegrasyonu**: Direkt slicer export
- [ ] 📊 **Analiz Araçları**: Baskı maliyeti hesaplama

## 📄 Lisans

Bu proje **GPL-3.0** lisansı altında yayınlanmıştır. Detaylar için [LICENSE](../LICENSE) dosyasını inceleyin.

```
3D Print Connector - Blender Addon for Tenon-Mortise Connections
Copyright (C) 2024 Mustafa Akin

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License.
```

## 👨‍💻 Geliştirici

**Mustafa Akin**
- 📧 Email: [makin38@gmail.com](mailto:makin38@gmail.com) | [makin38@hotmail.com](mailto:makin38@hotmail.com)
- 🐱 GitHub: [@makin38](https://github.com/makin38)

## 🙏 Teşekkürler

- **Blender Foundation**: Harika 3D yazılımı için
- **3D Printing Community**: Test ve geri bildirimler için
- **Open Source Community**: İlham ve destek için

---

## 🚀 Hemen Deneyin!

```bash
# Hızlı test için:
1. İki küp oluşturun (Add > Mesh > Cube)
2. Üçüncü küpü konnektör olarak kullanın
3. Eklentiyi çalıştırın!
```

**⭐ Projeyi beğendiyseniz star vermeyi unutmayın!**

---

*Bu eklenti sevgi ❤️ ve çok kahve ☕ ile geliştirilmiştir.*
