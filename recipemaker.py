from sys import argv

script,filename = argv

recipename = input("Recipe name: ")
preptime = int(input("Prep time in minutes: "))
cooktime = int(input("Cook time in minutes: "))
totaltime = (preptime + cooktime) 

target = open(filename, 'w')

target.write(f"""
<?xml version='1.0' encoding='utf-8'?>
<html xmlns="http://www.w3.org/1999/xhtml">
    <head>
        <title>{recipename}</title>
        <link type="text/css" rel="stylesheet" href="page_styles.css"/> 
        <link type="text/css" rel="stylesheet" href="stylesheet.css"/> 
    </head>

    <body>
        <hr>
        <h2>{recipename}</h2>

        <table width="100%">
            <tr>
                <th align="center">Prep Time</th>
                <th align="center">Cook Time</th>
                <th align="center">Total Time</th>
            </tr>
            <tr>
            <tr>
                <td align="center">{preptime} mins</td>
                <td align="center">{cooktime} mins</td>
                <td align="center">{totaltime} mins</td>
            </tr>
        </table>
        </hr>

        <hr>
            <h3>Ingredients</h3>
            <ul>
"""
             )
print("List off them ingredients, put a '.' at the prompt when finished.")

while (True):
    ingredient = input("> ")
    if (ingredient == "."):
        break
    target.write(f"\t\t\t\t<li>{ingredient}</li>\n")

target.write("""
            </ul>
        </hr>

        <hr>
            <h3>Instructions</h3>
            <ol>
""")

print("Give the steps, enter '.' to end. ")

while(True):
    step = input("> ")
    if (step == ".") :
        break
    target.write(f"\t\t\t\t<li>{step}</li>\n")

target.write("""
            </ol>
        </hr>

    </body>
</html>
""")
target.close()
