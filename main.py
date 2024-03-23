from texture_mapper import TextureMapper

# driver function 
if __name__=="__main__": 
    mapper = TextureMapper(canvas="./img/canvas.jpeg", texture="./img/texture.png")
    mapper.get_map()
    mapper.map()
