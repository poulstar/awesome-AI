a = "Year,Industry_aggregation_NZSIOC,Industry_code_NZSIOC,Industry_name_NZSIOC,Units,Variable_code,Variable_name,Variable_category,Value,Industry_code_ANZSIC06"
b = """
2021,Level 1,99999,All industries,Dollars (millions),H01,Total income,Financial performance,"757504","ANZSIC06 divisions A-S (excluding classes K6330, L6711, O7552, O760, O771, O772, S9540, S9601, S9602, and S9603)"
"""

print(len(a.split(",")))
print(len(b.split(",")))