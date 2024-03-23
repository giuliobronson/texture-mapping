from texture_mapper import TextureMapper

# driver function 
if __name__=="__main__": 

    mapper = TextureMapper(canvas="cuadros_branco.jpeg", texture="cuadros_branco.jpeg")
    mapper.get_map()
    mapper.map()
