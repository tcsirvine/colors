import turtle

def getGradient():
  colors = []
  rgb = [255, 0, 0]
  rateofchange =  10
  for i in range(2):
    for j in range(255/rateofchange):
      rgb[i + 1] += rateofchange
      colors.append(list(rgb))     
    
    rgb[i + 1] = 255
    
    for j in range(255/rateofchange):
      rgb[i] -= rateofchange
      colors.append(list(rgb))
    
    rgb[i] = 0
  
  return colors

colors = getGradient()
turtle.speed(0)

for i in range(1000):
  index = int(i/10) % len(colors)
  color = colors[index]
  turtle.color(color)
  turtle.forward(i)
  turtle.right(95)
