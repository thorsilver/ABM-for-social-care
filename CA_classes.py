import re

classI = [0,8,32,40,128,136,160,168,255,64,239,253,251,96,235,249,254,192,238,252,250,224,234,248]
classII = [1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15, 19, 23, 24, 25, 26, 27, 28, 29, 33, 34, 35, 36, 37, 38, 42, 43, 44, 46, 50, 51, 56, 57, 58, 62, 72, 73, 74, 76, 77, 78, 94, 104, 108, 130, 132, 134, 138, 140, 142, 152, 154, 156, 162, 164, 170, 172, 178, 184, 200,
204, 232,127,16,191,247,17,63,119,223,95,20,159,215,21,31,87,65,111,125,80,175,245,47,81,117,68,207,221,69, 79, 93,84, 143, 213,85,55,66, 189, 231,61, 67, 103,82, 167, 181,39, 53, 83,70, 157, 199,71,123,48, 187, 243,49, 59, 115,219,91,52, 155, 211,112, 171, 241,113,100, 
203, 217,116, 139, 209,179,98, 185, 227,99,114, 163, 177,118, 131, 145,237,109,88, 173, 229,205,92, 141, 197,133,244,233,201,144, 190, 246,222,148, 158, 214,174, 208, 224,196, 206, 220,212,188, 194, 230,166, 180, 210,198,176, 186, 242,218,240,202, 216, 228,226,236]
classIII=[18,22,30,45,60,90,105,122,126,146,150,183,151,86,135,149,75,89,101,102,153,195,165,161,129,182]
classIV=[41,54,106,110,97,107,121,147,120,169,225,124,137,193]

classI.sort()
classII.sort()
classIII.sort()
classIV.sort()

def merge_two_dicts(x, y):
    """Given two dicts, merge them into a new dict as a shallow copy."""
    z = x.copy()
    z.update(y)
    return z

classIdict = dict.fromkeys(classI,1)
classIIdict = dict.fromkeys(classII,2)
classIIIdict = dict.fromkeys(classIII,3)
classIVdict = dict.fromkeys(classIV,4)

classI_II = merge_two_dicts(classIdict, classIIdict)
classI_II_III = merge_two_dicts(classI_II, classIIIdict)
classI_II_III_IV = merge_two_dicts(classI_II_III, classIVdict)

class_list_ordered = classI_II_III_IV.values()

final_text = str(class_list_ordered)
# final_text.replace(':',' ->')

with open("CA class data.txt", "w") as text_file:
    text_file.write(final_text)
    # text_file.write(str(classIdict) + "\n")
    # text_file.write(str(classIIdict) + "\n")
    # text_file.write(str(classIIIdict) + "\n")
    # text_file.write(str(classIVdict) + "\n")

print(str(len(class_list_ordered)))