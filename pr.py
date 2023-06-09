import os

def select_profile_series():
    print("Serii de profil disponibile:")
    print("1. IV64")
    print("2. IV64 Ancienne")
    print("3. IV68")
    print("4. IV78")
    print("5. IV92")
    print("6. IV68 wood alu")
    print("7. IV78 wood alu")
    print("8. IV78 wood alu Soft")

    profile_series = input("Selecta?i seria de profil doritã (1-8): ")
    return profile_series

def select_thermal_coefficient():
    print("Coeficien?i termici disponibili:")
    print("1. 1.3 W/m2k")
    print("2. 1 W/m2k")
    print("3. 0.8 W/m2k")

    thermal_coefficient = input("Selecta?i coeficientul termic dorit (1-3): ")
    return thermal_coefficient

def select_soundproof_coefficient():
    print("Coeficien?i fonicã disponibili:")
    print("1. 30 dB")
    print("2. 32 dB")
    print("3. 35 dB")
    print("4. 38 dB")
    print("5. 40 dB")
    print("6. 42 dB")
    print("7. 45 dB")
    print("8. 48 dB")
    print("9. 50 dB")

    soundproof_coefficient = input("Selecta?i coeficientul fonic dorit (1-9): ")
    return soundproof_coefficient

def select_material(profile_series):
    materials = ["molid", "pin nordic", "meranti", "stejar", "accoya"]
    if profile_series == "1" or profile_series == "2" or profile_series == "4":
        materials = materials[:4]
    elif profile_series == "6" or profile_series == "7" or profile_series == "8":
        materials = materials[:2]

    print("Materiale disponibile:")
    for i, material in enumerate(materials):
        print(f"{i+1}. {material}")

    material = input("Selecta?i materialul dorit (1-{len(materials)}): ")
    return materials[int(material)-1]

def select_glazing(profile_series):
    glazing_options = ["vitraj dublu cu emisivitate redusã", "vitraj dublu cu protec?ie solarã"]
    if profile_series == "3" or profile_series == "5" or profile_series == "6" or profile_series == "7" or profile_series == "8":
        glazing_options.append("vitraj triplu cu emisivitate redusã")
        glazing_options.append("vitraj triplu cu protec?ie solarã")

    print("Op?iuni de vitraj disponibile:")
    for i, option in enumerate(glazing_options):
        print(f"{i+1}. {option}")

    glazing = input("Selecta?i op?iunea de vitraj doritã (1-{len(glazing_options)}): ")
    return glazing_options[int(glazing)-1]

def select_number_of_frames(opening_type):
    if opening_type in ["batant", "oscilo-batant", "glisant", "oscilo-culisant", "glisantã prin ridicare"]:
    num_frames = input("Introduce?i numãrul de cercevele (1 sau 2): ")
    elif opening_type == "pivotant":
        num_frames = "1"
    elif opening_type == "armonicã":
        print("Op?iuni de numãr de cercevele disponibile:")
        print("1. 1")
        print("2. 2")
        print("3. 3")
        print("4. 4")
        print("5. 5")
        print("6. 6")
        print("7. 7")

        num_frames = input("Selecta?i numãrul de cercevele dorit (1-7): ")

    return num_frames

def enter_dimensions():
    width = input("Introduce?i lã?imea tocului: ")
    height = input("Introduce?i înãl?imea tocului: ")
    parapet_height = input("Introduce?i înãl?imea parapetului: ")

    return width, height, parapet_height

def upload_file():
    file_path = input("Introduce?i calea fi?ierului PDF/JPG: ")
    # Verificã dacã fi?ierul existã
    if os.path.exists(file_path):
        # Implementeazã logica pentru procesarea fi?ierului
        print("Fi?ierul a fost încãrcat cu succes.")
    else:
        print("Fi?ierul nu a fost gãsit.")

# Func?ia principalã
def main():
    profile_series = select_profile_series()
    thermal_coefficient = select_thermal_coefficient()
    soundproof_coefficient = select_soundproof_coefficient()
    material = select_material(profile_series)
    glazing = select_glazing(profile_series)
    opening_type = input("Introduce?i tipul de deschidere: ")
    num_frames = select_number_of_frames(opening_type)
    width, height, parapet_height = enter_dimensions()
    upload_file()

    # Afiseaza toate detaliile selectate
    print("Detalii selectate:")
    print(f"Seria de profil: {profile_series}")
    print(f"Coeficient termic: {thermal_coefficient}")
    print(f"Coeficient fonic: {soundproof_coefficient}")
    print(f"Material: {material}")
    print(f"Vitraj: {glazing}")
    print(f"Tipul de deschidere: {opening_type}")
    print(f"Numãrul de cercevele: {num_frames}")
    print(f"Lã?ime toc: {width}")
    print(f"Înãl?ime toc: {height}")
    print(f"Înãl?ime parapet: {parapet_height}")

# Apelarea func?iei principale
if __name__ == "__main__":
    main()