class ZeldaMap:
  def __init__(self, width, height, gridlist):
    self.width = width
    self.height = height
    self.gridlist = gridlist

  def generate_divlist(self):
    mapstring = '<div id="zeldamap">'
    for n in self.gridlist:
      mapstring += '<span class="tile tile_'+ str(n) + '"></span>'
    #print mapstring + '</div>'
    files = open('TESTMAP.html','w')
    files.write('<link rel="stylesheet" href="TESTMAP.css" type="text/css" />'+mapstring+'</div>')

  def generate_css(self):
    files = open('TESTMAP.css','w')  
    files.write('#zeldamap {\n'+'  position:relative;\n'+ '  width:'+str(self.width*16)+'px;\n'+ '  height:'+str(self.height*16)+'px;\n'+ '  border: none;\n'+ '}\n'+ '\n'+ '.tile {\n'+ '  z-index:10;\n'+'  display:inline-block;\n'+ '  width: 16px;\n'+ '  height:16px;\n'+ '  margin: 0px;\n'+ '  padding:0px;}\n\n')
    for n in set(self.gridlist):
      bigX,bigY = n%24, n/24
      x,y       = 17*bigX+1, 17*bigY+1
      files.write('.tile_' + str(n) + ' {background:url(sprites/la_overtile.png) -'+str(x)+'px -'+str(y)+'px no-repeat;}\n')


