
// Hax que me encontre para imprimir dizque para imprimir los json bien bonitos
// falta el lint
// sin eso -> no hace nada laverdad ...
/*
function printPrettyJSON() {
      //var badJSON = document.getElementById('prettyJSONFormat').value;
      // by class ? -> map [] of all
      var parseJSON = JSON.parse(badJSON.prettyPrint());
      var JSONInPrettyFormat = JSON.stringify(parseJSON, undefined, 4);
      document.getElementById('prettyJSONFormat').value =
      JSONInPrettyFormat;
}

// esta funcion -> funciona mal : no hace lo que uno creeria que hace... ni idea....

function usarEjemplo(){
    var promptinput = document.getElementById('promptEjemplo');
    promptinput.value = `titanical cyborg giant squid 
escaping alien toxic vegetation, 
intricate Three-point lighting portrait, 
by Ching Yeh and Greg Rutkowski, detailed cyberpunk 
in the style of GitS 1995`
}



function activarDarkMode(){
    //var darkButton = document.getElementById('darkBtn');
    if !DarkReader.isEnabled(){
        DarkReader.enable({contrast: 5})
    } else {
        DarkReader.disable();
    }
}

 */

function activarDarkMode(){
    const el = document.body
    el.classList.toggle("dark-modo")
    let images = document.querySelectorAll("img");

    // haxito para revertir  invert global effect: A,B -> B,A ::
    images.forEach((imagen) => {
        //imagen.style.filter = "invert(100%) hue-rotate(0.5turn)";
        imagen.classList.toggle("dark-image")
        // a class containing that.
    }) // -> hue shift can make up NICE effects. for sure

}