cmPerInch = (2.54)
inchesPerFeet = (12)

def HeightFtInToCm(heightFt,heightIn):
    intHeightFt = int(heightFt)
    intHeightIn = int(heightIn)
    totalInches = (intHeightFt * inchesPerFeet) + intHeightIn
    heightCm = totalInches * cmPerInch
    return heightCm

heightFt = input("How tall are you in feet?: ")
heightIn = input("How tall are you in inches?: ")
heightCm = HeightFtInToCm(heightFt,heightIn)

print("You are",round(heightCm,2),"cm tall!")
