import replicate

# : export replicate api key

def generarImagen(prompt: str):
    model = replicate.models.get("stability-ai/stable-diffusion")
    res_imgUrl = model.predict(prompt=prompt)
    print(res_imgUrl)
    return res_imgUrl


