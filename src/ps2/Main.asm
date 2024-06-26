// PlayStation 2 "Shinseiki GPX Cyber Formula: Road to the Evolution" Japanese To English Translation

endian lsb // PlayStation 2 EE requires Little-Endian Encoding (Least Significant Bit)
output "../../output/Shinseiki GPX Cyber Formula [E].iso", create
origin $000000; insert "../../input/Shinseiki GPX Cyber Formula [J].iso" // Include Japanese Cyber Formula ISO

macro Text(OFFSET, TEXT) {
  map 0, 0, 256 // Map Default ASCII Chars
  map '|', 0x00 // End of string 

  origin {OFFSET}
  
  //while (read({OFFSET} + str.len(TEXT)) != 0x00) {
  //  {TEXT} += 0x00
  //}

  db {TEXT} // ASCII Text To Print

}

macro TextShiftJIS(OFFSET, TEXT) {
  // Map Shift-JIS Words
  map ' ',  $8140
  map $2C,  $8143 // Comma ","
  map '.',  $8144
  map ':',  $8146
  map '?',  $8148
  map '!',  $8149
  map '~',  $8160
  map '\s', $8166 // Single Quote "'"
  map '\d', $8168 // Double Quote '"'
  map '+',  $817B
  map '&',  $8195
  map '0',  $824F, 10 // Map Numbers
  map 'A',  $8260, 26 // Map English "Upper Case" Characters
  map 'a',  $8281, 26 // Map English "Lower Case" Characters

  origin {OFFSET}
  dw {TEXT} // Shift-JIS Text To Print
}

//Not a real assert, just prints the error message in console and doesn't compile further
macro Assert(MESSAGE) {
  "{MESSAGE}\n"
}

macro ReplaceAsset(ORIGIN, FILE, SIZE) {
  if !file.exists({FILE}) {
    print "{FILE} doesn't exist!"
  } else if file.exists({FILE}) {
    if (file.size({FILE}) > {SIZE} && {SIZE} != -1) {
      Assert("File {FILE} is bigger than Size {SIZE}")
    } else if (file.size({FILE}) <= {SIZE}) {
      origin {ORIGIN}
      insert {FILE}
      fill {SIZE} - file.size({FILE})
    }
  }
}

//Region
Text($82A51, "U")
Text($84A24, "U")
Text($93812, "U")
Text($3CB014, "U")

//include "Banner.asm"
//include "Menu.asm"
//include "System.asm"
include "Txtd.asm"