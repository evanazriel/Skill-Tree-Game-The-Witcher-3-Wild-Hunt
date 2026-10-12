## Analisis Relasi dan Urutan Parsial pada Skill Tree Game The Witcher 3: Wild Hunt

Mata kuliah Matematika Diskrit diampu oleh : Andri Rahadyan S.Pd., M.Si 

## Identitas Kelompok

| No | NIM          | Nama Lengkap                  |
| -- | ------------ | ----------------------------- |
| 1  | 202543500183 | Evan Azriel Devtriyan         |
| 2  | 202543500195 | Razan Maulana Hakim           |
| 3  | 202543500194 | Zhyzho Putra William          |

## Deskripsi 

Repositori ini berisi pemodelan matematis dan implementasi program untuk menganalisis sistem Skill Tree pada game The Witcher 3: Wild Hunt. Dalam game ini, pembukaan suatu kemampuan (skill) memerlukan prasyarat kemampuan sebelumnya serta investasi poin tertentu. Proyek ini memetakan mekanisme tersebut menggunakan konsep Matematika Diskrit—khususnya Teori Himpunan, Relasi Biner, Graf Berarah (Directed Graph), Urutan Parsial (Partial Order), dan Transitive Closure.

## Konsep yang Diterapkan 
1. Himpunan Objek ($A$): Kumpulan skill utama (Muscle Memory, Precise Blows, Resolve, Active Shield, Metabolism    Control, Acquired Tolerance).

2. Himpunan Kategori ($B$): Kumpulan skill utama (Combat, Signs, Alchemy, General).

3. Relasi Biner ($R$): Hubungan prasyarat (prerequisite) antar-skill (makna: "Skill $A$ harus dibuka sebelum Skill $B$").

4. Analisis Sifat Relasi: Pembuktian sifat Irefleksif, Antisimetris, dan Transitif untuk memastikan hierarki skill tidak memiliki siklus (Directed Acyclic Graph / DAG).

5. Transitive Closure (Algoritma Warshall): Menghitung seluruh skill lanjutan yang dapat diakses secara langsung maupun tidak langsung dari suatu skill awal.

6. Urutan Parsial & Urutan Topologi (Topological Sort): Menentukan urutan prioritas atau build order optimal bagi pemain untuk membuka skill secara runtut.

# Tools 
1. Python 
2. NumPy
3. NetworkX

## Requirements
- Python Version 3.14.1 or newer

## How To Install
```bash
git clone https://github.com/evanazriel/Skill-Tree-Game-The-Witcher-3-Wild-Hunt.git
```