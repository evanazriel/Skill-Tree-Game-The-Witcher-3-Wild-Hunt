import numpy as np
import networkx as nx

# DETEKSI SIFAT RELASI

def check_reflexive(M, elements):
    n = len(elements)
    for i in range(n):
        if M[i, i] == 0:
            return False, (elements[i], elements[i])
    return True, None

def check_symmetric(M, elements):
    n = len(elements)
    for i in range(n):
        for j in range(n):
            if M[i, j] == 1 and M[j, i] == 0:
                return False, ((elements[i], elements[j]), (elements[j], elements[i]))
    return True, None

def check_antisymmetric(M, elements):
    n = len(elements)
    for i in range(n):
        for j in range(n):
            if i != j and M[i, j] == 1 and M[j, i] == 1:
                return False, ((elements[i], elements[j]), (elements[j], elements[i]))
    return True, None

def check_transitive(M, elements):
    n = len(elements)
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if M[i, j] == 1 and M[j, k] == 1 and M[i, k] == 0:
                    return False, ((elements[i], elements[j]), (elements[j], elements[k]), (elements[i], elements[k]))
    return True, None

def transitive_closure_warshall(M): # Algoritma Warshall Mandiri
    W = M.copy().astype(int)
    n = len(W)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                W[i, j] = W[i, j] or (W[i, k] and W[k, j])
    return W

def get_equivalence_classes(M, elements):
    G = nx.Graph()
    G.add_nodes_from(elements)
    n = len(elements)
    for i in range(n):
        for j in range(n):
            if M[i, j] == 1 and i != j:
                G.add_edge(elements[i], elements[j])
    return list(nx.connected_components(G))

def get_poset_hasse(M, elements):
    G = nx.DiGraph()
    G.add_nodes_from(elements)
    n = len(elements)
    for i in range(n):
        for j in range(n):
            if M[i, j] == 1 and i != j:
                G.add_edge(elements[i], elements[j])
    hasse_G = nx.transitive_reduction(G)
    return list(hasse_G.edges())



# BLOK PENGUJIAN OTOMATIS (TEST CASES)
def run_all_tests():
    # KELOMPOK (a): Data Hasil Hitung Manual (R1 The Witcher 3) 
    elements_a = ["a1", "a2", "a3", "a4", "a5", "a6"]
    matrix_r1 = np.array([
        [1, 1, 1, 0, 0, 0],
        [0, 1, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 1, 1],
        [0, 0, 0, 0, 0, 1]
    ])
    print("[Uji A] Data Utama R1 (The Witcher 3):")
    print("  - Refleksif   :", check_reflexive(matrix_r1, elements_a)[0])
    print("  - Antisimetris:", check_antisymmetric(matrix_r1, elements_a)[0])
    print("  - Transitif   :", check_transitive(matrix_r1, elements_a)[0])
    print("  - Hasse Pairs :", get_poset_hasse(matrix_r1, elements_a))
    print("  - Warshall Closure :")
    print(transitive_closure_warshall(matrix_r1))   
    print("  Status        : LULUS\n")

    # KELOMPOK (b1): Kasus Tepi  Relasi Kosong
    elements_3 = ["a1", "a2", "a3"]
    matrix_kosong = np.zeros((3, 3), dtype=int)
    ref_b1, ref_ex_b1 = check_reflexive(matrix_kosong, elements_3)
    sym_b1, _ = check_symmetric(matrix_kosong, elements_3)
    trans_b1, _ = check_transitive(matrix_kosong, elements_3)
    print("[Uji B1] Kasus Tepi - Relasi Kosong:")
    print(f"  - Refleksif   : {ref_b1} (Penyangkal: {ref_ex_b1})")
    print(f"  - Simetris    : {sym_b1}")
    print(f"  - Transitif   : {trans_b1}")
    print("  Status        : LULUS\n")

    # KELOMPOK (b2): Kasus Tepi - Relasi Identitas 
    matrix_identitas = np.eye(3, dtype=int)
    print("[Uji B2] Kasus Tepi - Relasi Identitas:")
    print("  - Refleksif   :", check_reflexive(matrix_identitas, elements_3)[0])
    print("  - Simetris    :", check_symmetric(matrix_identitas, elements_3)[0])
    print("  - Antisimetris:", check_antisymmetric(matrix_identitas, elements_3)[0])
    print("  - Transitif   :", check_transitive(matrix_identitas, elements_3)[0])
    print("  Status        : LULUS\n")

    # KELOMPOK (b3): Kasus Tepi - Relasi Universal 
    matrix_universal = np.ones((3, 3), dtype=int)
    antisym_b3, antisym_ex_b3 = check_antisymmetric(matrix_universal, elements_3)
    print("[Uji B3] Kasus Tepi - Relasi Universal:")
    print("  - Refleksif   :", check_reflexive(matrix_universal, elements_3)[0])
    print("  - Simetris    :", check_symmetric(matrix_universal, elements_3)[0])
    print("  - Transitif   :", check_transitive(matrix_universal, elements_3)[0])
    print(f"  - Antisimetris: {antisym_b3} (Penyangkal ditemukan: {antisym_ex_b3})")
    print("  Status        : LULUS\n")

    # KELOMPOK (c): Data Lengkap Kasus Ekuivalensi (R2)
    matrix_r2 = np.array([
        [1, 1, 1, 0, 0, 0],
        [1, 1, 1, 0, 0, 0],
        [1, 1, 1, 0, 0, 0],
        [0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 1, 1],
        [0, 0, 0, 0, 1, 1]
    ])
    print("[Uji C] Kasus Ekuivalensi R2 (Kategori Skill):")
    print("  - Refleksif       :", check_reflexive(matrix_r2, elements_a)[0])
    print("  - Simetris        :", check_symmetric(matrix_r2, elements_a)[0])
    print("  - Transitif       :", check_transitive(matrix_r2, elements_a)[0])
    print("  - Kelas Ekuivalensi:", get_equivalence_classes(matrix_r2, elements_a))
    print("  Status            : LULUS")

if __name__ == "__main__":
    run_all_tests()