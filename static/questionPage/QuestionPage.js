





function displayQuestion(fullObject) {
    console.log(fullObject);
    const questionElement = document.getElementById('question_text');
    console.log(questionElement);
    questionElement.innerHTML = fullObject;
    console.log(fullObject.question);
    // questionElement.innerHTML = fullObject.question;
}
// function displayQuestion() {
//     const elementHtml = document.getElementById('to_JS').innerHTML;
//     const questionElement = document.getElementById('');
//     questionElement.innerHTML = elementHtml;
// }
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
function wrongAnswer() {
    const submitButton = document.querySelector('input[id="submit_button"]');
    const descriptionBox = document.getElementById('respone_box');
    const next_questionButton = document.getElementById('next_question');


    if (descriptionBox) {
        // Hide the description box initially
        descriptionBox.style.display = 'none';

        // Add an event listener to the submit button
        submitButton.addEventListener('click', function(event) {
            // Prevent the form from submittings
            event.preventDefault();
            descriptionBox.style.display = 'block';
            descriptionBox.style.color = 'red';
            
            submitButton.style.display = 'none';

        });
    } else {
        console.error("Element with id 'respone_box' not found");
    }
}

    
// function wrongAnswer() {
//     const submitButton = document.querySelector('input[type="submit"]');
//     const descriptionBox = document.getElementById('respone_box');

//     if (descriptionBox) {
//         // Hide the description box initially
//         descriptionBox.style.display = 'none';

//         // Add an event listener to the submit button
//         submitButton.addEventListener('click', function(event) {
//             // Prevent the form from submitting
//             event.preventDefault();
//             descriptionBox.style.display = 'block';
//             descriptionBox.style.backgroundColor = 'red';
//         });
//     } else {
//         console.error("Element with id 'respone_box' not found");
//     }
// }

// function listen to button id nextquestion

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





function displayQuestion(question_list,index) {
    if (index >= question_list.length) {
        return alert('No more questions');
    }
    let currentQuestion = question_list[index].question;
    const questionElement = document.getElementById('question_text');
    
    questionElement.innerHTML = currentQuestion;
    
    
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

    all_list = shuffleArray(all_list);

    for (let i = 0; i < all_list.length; i++) {
        all_list[i].innerHTML = all_choice[i];
        all_value[i].value = all_choice[i];
    }




}
// __main__
document.addEventListener('DOMContentLoaded', function() {
    // get the data
    const elementHtml = document.getElementById('to_JS').innerHTML;
    const full_object = JSON.parse(elementHtml);
    console.log(full_object);

    let index = 0;
    const nextQuestionButton = document.getElementById('next_question');
    checkAnswer();
    // when next question button is clicked
    nextQuestionButton.addEventListener('click', function(event) {
        event.preventDefault();
        
        
        displayQuestion(full_object,index);
        index = index + 1;
        
        displayChoice(full_object[index].incorrect_list,full_object[index].correct);


        // reset form
        document.getElementById("question_form").reset();
        resetAnswer();
        
    })
    
    

 
    

    //correctAnswer()
    



});

