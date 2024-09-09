
        /* Pregunta: ¿Cuál es la función de 'document.getElementById' en JavaScript? */
        /*acceder a algo del html basandote en un id*/
        function checkAnswer() {
            /* Pregunta: ¿Qué hace 'prompt' y cómo se puede usar en lugar de 'alert'? */
            /* coloca un cuadro de texto en el ejemplo de abajo para que se ingrese una respuesta por ejemplo*/
            let answer = prompt("Enter your answer:");

            /* Pregunta: ¿Cuál es el propósito de la instrucción 'if' en este fragmento de código? */
            /*para comparar si la respuesta ingresada en la linea anterior coincide con la que debe ser*/
            if (answer.toLowerCase() === 'paris') {
                alert("Correct!");
            } else {
                alert("Try again!");
            }
        }

        /* Pregunta: ¿Cómo se puede manipular el DOM usando JavaScript para cambiar el contenido de un elemento? */
        /* */
        document.getElementById("question").innerText = "What is the capital of Spain?";
