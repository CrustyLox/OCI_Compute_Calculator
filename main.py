import requests
# API endpoint
url = "https://apexapps.oracle.com/pls/apex/cetools/api/v1/products/"
response = requests.get(url)
data = response.json()

#cpu, ram, storage(could be boot)
# Target filters
shape_to_part_numbers = {
    'VM.Standard.A2.Flex': ['B109529', 'B109530'],
    'BM.Standard.E6.256': ['B111129', 'B111130'],
    'VM.Standard.E6.Flex': ['B111129', 'B111130'],
    'BM.Standard.E3.128': ['B92306', 'B92307'],
    'CI.Standard.E3.Flex': ['B92306', 'B92307'],
    'DVH.Standard.E3.128': ['B92306', 'B92307'],
    'Pod.Standard.E3.Flex': ['B92306', 'B92307'],
    'VM.Standard.E3.Flex': ['B92306', 'B92307'],
    'BM.Standard.E4.128': ['B93113', 'B93114'],
    'CI.Standard.E4.Flex': ['B93113', 'B93114'],
    'DVH.Standard.E4.128': ['B93113', 'B93114'],
    'Pod.Standard.E4.Flex': ['B93113', 'B93114'],
    'PostgreSQL.VM.Standard.Flex.E4': ['B93113', 'B93114'],
    'PostgreSQL.VM.Standard.Flex.E4.16.256GB': ['B93113', 'B93114'],
    'PostgreSQL.VM.Standard.Flex.E4.2.32GB': ['B93113', 'B93114'],
    'PostgreSQL.VM.Standard.Flex.E4.32.512GB': ['B93113', 'B93114'],
    'PostgreSQL.VM.Standard.Flex.E4.4.64GB': ['B93113', 'B93114'],
    'PostgreSQL.VM.Standard.Flex.E4.64.1024GB': ['B93113', 'B93114'],
    'PostgreSQL.VM.Standard.Flex.E4.8.128GB': ['B93113', 'B93114'],
    'VM.Standard.E4.Flex': ['B93113', 'B93114'],
    'BM.DenseIO.E4.128': ['B93121', 'B93122', 'B93123'],
    'VM.DenseIO.E4.Flex': ['B93121', 'B93122', 'B93123'],
    'BM.Standard.A1.160': ['B93297', 'B93298'],
    'Pod.Standard.A1.Flex': ['B93297', 'B93298'],
    'VM.Standard.A1.Flex': ['B93297', 'B93298'],
    'CI.Standard.A1.Flex': ['B93297', 'B93298'],
    'BM.Optimized3.36': ['B93311', 'B93312'],
    'DVH.Optimized3.36': ['B93311', 'B93312'],
    'VM.Optimized3.Flex': ['B93311', 'B93312'],
    'BM.Standard3.64': ['B94176', 'B94177'],
    'DVH.Standard3.64': ['B94176', 'B94177'],
    'PostgreSQL.VM.Standard3.Flex': ['B94176', 'B94177'],
    'PostgreSQL.VM.Standard3.Flex.16.256GB': ['B94176', 'B94177'],
    'PostgreSQL.VM.Standard3.Flex.2.32GB': ['B94176', 'B94177'],
    'PostgreSQL.VM.Standard3.Flex.32.512GB': ['B94176', 'B94177'],
    'PostgreSQL.VM.Standard3.Flex.4.64GB': ['B94176', 'B94177'],
    'PostgreSQL.VM.Standard3.Flex.8.128GB': ['B94176', 'B94177'],
    'VM.Standard3.Flex': ['B94176', 'B94177'],
    'BM.Standard.E5.192': ['B97384', 'B97385'],
    'DVH.Standard.E5.192': ['B97384', 'B97385'],
    'VM.Standard.E5.Flex': ['B97384', 'B97385'],
    'BM.DenseIO.E5.128': ['B98202', 'B98203', 'B98204'],
    'VM.DenseIO.E5.Flex': ['B98202', 'B98203', 'B98204'],
    'BM.DenseIO2.52': ['B88515'],
    'BM.GPU.A10.4': ['B95909'],
    'BM.GPU.A100-v2.8': ['B95907'],
    'BM.GPU.B200.8': ['B110978'],
    'BM.GPU.GB200.4 (NVL72)': ['B110979'],
    'BM.GPU.H100.8': ['B98415'],
    'BM.GPU.H200.8': ['B110519'],
    'BM.GPU.L40S.4': ['B109479'],
    'BM.GPU.MI300X.8': ['B109485'],
    'BM.GPU2.2': ['B88517'],
    'BM.GPU3.8': ['B89734'],
    'BM.GPU4.8': ['B92740'],
    'BM.HPC.E5.144': ['B96531'],
    'BM.HPC2.36': ['B90398'],
    'BM.Standard2.52': ['B88513'],
    'DVH.DenseIO2.52': ['B88515'],
    'DVH.Standard.E2.64': ['B90425'],
    'DVH.Standard2.52': ['B88513'],
    'VM.DenseIO1.16': ['B88516'],
    'VM.DenseIO1.4': ['B88516'],
    'VM.DenseIO1.8': ['B88516'],
    'VM.DenseIO2.16': ['B88516'],
    'VM.DenseIO2.24': ['B88516'],
    'VM.DenseIO2.8': ['B88516'],
    'VM.GPU.A10.1': ['B95909'],
    'VM.GPU.A10.2': ['B95909'],
    'VM.GPU2.1': ['B88518'],
    'VM.GPU3.1': ['B89734'],
    'VM.GPU3.2': ['B89734'],
    'VM.GPU3.4': ['B89734'],
    'VM.Standard2.1': ['B88514'],
    'VM.Standard2.16': ['B88514'],
    'VM.Standard2.2': ['B88514'],
    'VM.Standard2.24': ['B88514'],
    'VM.Standard2.4': ['B88514'],
    'VM.Standard2.8': ['B88514']
}
storage = "B96484" #boot volumes part number
vpu = "B91962" #production units part numbers

target_shape = input("Enter the shape: ")
target_currency = "INR"

part_numbers = [] # stores part numbers
if target_shape in shape_to_part_numbers:
    part_numbers = shape_to_part_numbers[target_shape]
else:
    print(f"Shape '{target_shape}' not found in the mapping.")
print(part_numbers)

#finding cpu
matching_cpu_items = [
    item for item in data["items"]
    if item.get("partNumber") == part_numbers[0]
]

#finding ram
if len(part_numbers) > 1:
    matching_ram_items = [
    item for item in data["items"]
    if item.get("partNumber") == part_numbers[1]
]
else: #no ram part means its bundeled along with cpu price
    matching_ram_items = 0


SOFlag = False # flag to see if shape is standard or VM.Optimized

#finding storage
if len(part_numbers) > 2:
    matching_storage_items = [
    item for item in data["items"]
    if item.get("partNumber") == part_numbers[2]
]
elif ('Standard' in target_shape) or ('Optimized' in target_shape): # standard and optimized parts use extra cloud(boot) storage
    SOFlag = True
    matching_storage_items = [
    item for item in data["items"]
    if item.get("partNumber") == storage
]
else: # no storage entirely means its bundled with cpu price
    matching_storage_items = 0
#finding vpu price
matching_vpu_items = [
    item for item in data["items"]
    if item.get("partNumber") == vpu
]


price_value = []#array of cpu,ram,storage,vpu prices


matching_items = [matching_cpu_items,matching_ram_items,matching_storage_items,matching_vpu_items]
for matching_item in matching_items:
    if  matching_item == 0:
        price_value.append(0)
    else:
        for item in matching_item:
            localizations = item.get("currencyCodeLocalizations", [])
            currency_entry = next((c for c in localizations if c.get("currencyCode") == target_currency), None)

            if currency_entry:
                prices = currency_entry.get("prices", [])
                price_entry = next((p for p in prices if p.get("model") == "PAY_AS_YOU_GO"), None)
                if price_entry and price_entry.get("value") is not None:
                    price_value.append(price_entry["value"])
                else:
                    print("INR pricing found but value is missing or model is not PAY_AS_YOU_GO.")
            else:
                print("No pricing found for INR.")
print(price_value)


#cpu prices always there so input cpu
cpu_count = int(input("Enter cpu count: "))


if price_value[1] == 0 and price_value[2] == 0: #if no ram and storage price given it will be bundled with cpu price
    hour_cost = cpu_count * price_value[0]


elif price_value[1] == 0 and price_value[2] !=0: #if no ram but storage given its usually standard or optimized 
    boot_count = int(input("Enter boot volume: "))
    vpu_count = int(input("Enter amount of performance units: "))
    hour_cost = cpu_count * price_value[0] + (price_value[2] + (vpu_count*price_value[3]))*boot_count/744


elif price_value[1] !=0 and SOFlag == True: #if ram given and standard or optimized
    ram_count = int(input("Enter ram count: "))
    boot_count = int(input("Enter boot volume: "))
    vpu_count = int(input("Enter amount of performance units: "))
    hour_cost = cpu_count * price_value[0] +ram_count*price_value[1] + (price_value[2] + (vpu_count*price_value[3]))*boot_count/744
elif price_value[1] != 0 and SOFlag == False: # when local disk storage given along with ram and cpu price
    ram_count = int(input("Enter ram count: "))
    boot_count = float(input("Enter local disk storage: "))
    hour_cost = cpu_count * price_value[0] +ram_count*price_value[1] + price_value[2]*boot_count

daily_cost = hour_cost*24
weekly_cost = hour_cost*24*7
monthly_cost = hour_cost*24*31
print("hourly cost: ",hour_cost)
print("daily cost",daily_cost)
print("weekly cost",weekly_cost)
print("monthly cost",monthly_cost)

