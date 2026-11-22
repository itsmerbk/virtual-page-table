from collections import OrderedDict

class MMU:
    def __init__(self, page_table, tlb_size=2):
        self.pt, self.tlb, self.cap = page_table, OrderedDict(), tlb_size
    def translate(self, vpn):
        if vpn in self.tlb: self.tlb.move_to_end(vpn); return self.tlb[vpn], "TLB_HIT"
        pfn = self.pt[vpn]; self.tlb[vpn] = pfn
        if len(self.tlb) > self.cap: self.tlb.popitem(last=False)
        return pfn, "PAGE_WALK"

if __name__ == "__main__":
    mmu = MMU({0: 14, 1: 29})
    assert mmu.translate(0)[1] == "PAGE_WALK" and mmu.translate(0) == (14, "TLB_HIT")
    print("[PASS] 068_virtual_page_table")
