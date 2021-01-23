#Program to accept filename from user and to print its extension
filename=input(" Input the Filename: ") #input the filename please enter full extension of the file
f_extns = filename.split(".") #splitting the name with its extension
print(" The extension of the file is :" + repr (f_extns[-1])) #printing the extension of the filename
