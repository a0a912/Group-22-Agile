


function resetAnswer() {
    const submitButton = document.querySelector('input[id="submit_button"]');
    const descriptionBox = document.getElementById('respone_box');
    const next_questionButton = document.getElementById('next_question');
    const answer = document.getElementById('answer');
    const description = document.getElementById('description');
    const submit_container = document.getElementById('submit_container');


    submit_container.style.alignItems = 'center';
    submit_container.style.display = 'inline-block';
    descriptionBox.style.display = 'none';
    submitButton.style.display = 'flex';
    next_questionButton.style.color = 'initial';
    next_questionButton.style.border = 'none'; 
    answer.innerText = '';
    description.innerText = '';
    submitButton.style.marginTop = '30px';
    submitButton.style.textAlign = 'center';
    submitButton.style.alignItems = 'center';
    
}

function description(result) {
    const submitButton = document.querySelector('input[id="submit_button"]');
    const descriptionBox = document.getElementById('respone_box');
    const next_questionButton = document.getElementById('next_question');
    const answer = document.getElementById('answer');
    const description = document.getElementById('description');

    if (result == true) {
        descriptionBox.style.backgroundColor = '#D7FFB8';
        next_questionButton.style.color = 'green';
        descriptionBox.style.color = 'green';
        next_questionButton.style.border = '2px solid green'; 
        answer.innerText = 'correct';
        description.innerText = "  let's go";
    }
    else {
        // descriptionBox.style.color = 'white';
        descriptionBox.style.backgroundColor = '#FFDFE0';
        next_questionButton.style.color = 'red';
        descriptionBox.style.color = 'red';
        next_questionButton.style.border = '2px solid red'; 
        answer.innerHTML = 'wrong';
    }
    descriptionBox.style.display = 'block';
    
    
    submitButton.style.display = 'none';

}


function shuffleArray(array) {
    return array.sort(() => Math.random() - 0.5);
}

function checkAnswer(correct) {
    var form = document.getElementById("question_form");

    form.addEventListener("submit", function(event) {
        event.preventDefault(); // Prevent form submission for this example

        var selectedOption = document.querySelector('input[name="choice"]:checked');
        if(selectedOption) {
            console.log("Selected value: ", selectedOption.value);

            if (selectedOption.value === correct) {
                console.log("Correct answer");
                description(true);
            } else {
                console.log("Wrong answer");
                description(false);
            }



      
            
        } else {
            console.log("No option selected");
        }
});
    
    
}






function displayChoice(incorrect_list,answer) {
    const choice1 = document.getElementById('choice1');
    const choice2 = document.getElementById('choice2');
    const choice3 = document.getElementById('choice3');
    const choice4 = document.getElementById('choice4');

    const input1 = document.getElementById('value1');
    const input2 = document.getElementById('value2');
    const input3 = document.getElementById('value3');
    const input4 = document.getElementById('value4');

    all_list = [choice1,choice2,choice3,choice4];
    all_choice = [incorrect_list[0],incorrect_list[1],incorrect_list[2],answer];
    all_value = [input1,input2,input3,input4];
    console.log(answer);

    all_choice = shuffleArray(all_choice);
    

    for (let i = 0; i < all_list.length; i++) {
        all_list[i].innerHTML = all_choice[i];
        all_value[i].value = all_choice[i];
    }





}

// __main__
document.addEventListener('DOMContentLoaded', function() {
    // get the data
    let point = 0;
    const score = document.getElementById('score_number');
    const elementHtml = document.getElementById('to_JS').innerHTML;
    const full_object = JSON.parse(elementHtml);
    console.log(full_object);
    

    let index = 0;
    const nextQuestionButton = document.getElementById('next_question');
    const form = document.getElementById("question_form");

    // Attach the form submit event listener once
    form.addEventListener("submit", function(event) {
        event.preventDefault(); // Prevent form submission

        var selectedOption = document.querySelector('input[name="choice"]:checked');
        if (selectedOption) {
            console.log("Selected value: ", selectedOption.value);

            if (selectedOption.value === full_object[index - 1].correct) {
                console.log("Correct answer");
                point += 1;
                score.innerHTML = point;
                
                description(true);

            } else {
                console.log("Wrong answer");
                description(false);
            }
        } else {
            console.log("No option selected");
        }
    });

    // Function to display the current question
    function displayQuestion(question_list, index) {
        if (index >= question_list.length) {
            return alert('No more questions');
        }
        let currentQuestion = question_list[index].question;
        const questionElement = document.getElementById('question_text');
        questionElement.innerHTML = currentQuestion;
    }



    // Initialize the first question
    displayQuestion(full_object, index);
    displayChoice(full_object[index].incorrect_list, full_object[index].correct);
    index++;

    // Event listener for next question button
    nextQuestionButton.addEventListener('click', function(event) {
        event.preventDefault();
        if (index < full_object.length) {
            displayQuestion(full_object, index);
            displayChoice(full_object[index].incorrect_list, full_object[index].correct);
            index++;
            document.getElementById("question_form").reset();
            resetAnswer();
        } else {
            alert('No more questions');
        }
    });
});




