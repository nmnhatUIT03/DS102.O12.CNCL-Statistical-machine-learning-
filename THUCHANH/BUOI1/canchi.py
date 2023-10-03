def tinh_can_chi(nam):
    can = ["CANH", "TAN", "NHAM", "QUY", "GIAP", "AT", "BINH", "DINH", "MAU", "KY"]
    chi = ["THAN", "DAU", "TUAT", "HOI", "TY'", "SUU", "DAN", "MEO", "THIN", "TY.", "NGO", "MUI"]
    
    can_index = nam  % 10
    chi_index = nam  % 12
    
    can_nam = can[can_index]
    chi_nam = chi[chi_index]
    
    if nam < 0:
        can_nam = can[can_index + 1]
        chi_nam = chi[chi_index + 1]
    
    return f"{can_nam} {chi_nam}"


nam = int(input())
ket_qua = tinh_can_chi(nam)
print(ket_qua)
