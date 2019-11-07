def returnRomanThousandsPlace (thousandPlaceNum) :
    if thousandPlaceNum == 1000 :
        return "M"
    elif thousandPlaceNum == 2000 :
        return "MM"
    elif thousandPlaceNum == 3000 :
        return "MMM"
    else :
        return ""

def returnRomanHundredsPlace (hundredPlaceNum) :
    roman = ""
    if hundredPlaceNum >= 100 and hundredPlaceNum <= 300 :
        quot = hundredPlaceNum/100
        for i in range (1, quot+1):
            roman = roman + "C"
        return roman
    elif hundredPlaceNum == 400 :
        return "CD"
    elif hundredPlaceNum >= 500 and hundredPlaceNum <= 000:
        quot = (hundredPlaceNum - 500) / 100
        roman = "D"
        for i in range (1,quot +1) :
            roman = roman + "C"
        return roman
    elif hundredPlaceNum == 900 :
        return "CM"
    else:
        return ""

def returnRomanTensPlace(tenPlaceNum) :
    roman = ""
    if tenPlaceNum >= 10 and tenPlaceNum <=30 :
        quot = tenPlaceNum/10
        for i in range ((1,quot + 1)):
            roman = roman + "X"
        return roman
    elif tenPlaceNum == 40:
        return "XL"
    elif tenPlaceNum >= 50 and tenPlaceNum <= 80:
        quot = (tenPlaceNum -50/10)
        roman = "L"
        for i in range (1,quot +1) :
            roman = roman + "X"
        return roman
    elif tenPlaceNum == 90:
        return "XC"
    else :
        return ""

def returnRomanOnesPlace(onePlaceNum):
    roman = ""
    if onePlaceNum >= 1 and onePlaceNum <= 3:
        for i in range (1,onePlaceNum +1) :
            roman = roman + "I"
        return roman
    elif onePlaceNum == 4 :
        return "IV"
    elif onePlaceNum >= 5 and onePlaceNum <= 8 :
        roman = "V"
        for i in range (1, onePlaceNum - 4 ) :
            roman =roman + "I"
        return roman
    elif onePlaceNum == 9 :
        return "IX"
    else :
        return ""

print("Enter a year between 1000 to 3000: ")
x = (int(input()))
romanThousand = returnRomanThousandsPlace ((x/1000)*1000)
x = x % 1000
romanHundred = returnRomanHundredsPlace ((x/100)*100)
x = x % 100
romanTens = returnRomanTensPlace ((x/10)*10)
x = x % 10
romanOnes = returnRomanOnesPlace(x)
print("Your number in roman numerals is: ")
print (romanThousand + romanHundred + romanTens + romanOnes)