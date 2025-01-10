photowaist = float(input(("How wide is the photo at waist? ")))
photocutout = float(input(("How wide is the photo cutout? ")))

photocutoutratio = photocutout / photowaist
print(photocutoutratio)

realwaist = float(input("What is the width of pattern piece at waist? "))
print("cut out width is " + str(realwaist * photocutoutratio) + "cm.")
