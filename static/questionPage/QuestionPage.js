





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


function correctAnswer() {
    const submitButton = document.querySelector('input[id="submit_button"]');
    const descriptionBox = document.getElementById('respone_box');
    const next_questionButton = document.getElementById('next_question');
    const answer = document.getElementById('answer');
    const description = document.getElementById('description');

    if (descriptionBox) {
        // Hide the description box initially
        descriptionBox.style.display = 'none';

        // Add an event listener to the submit button
        submitButton.addEventListener('click', function(event) {
            // Prevent the form from submitting
            event.preventDefault();
            descriptionBox.style.display = 'block';
            descriptionBox.style.color = 'green';
            descriptionBox.style.backgroundColor = '#D7FFB8';
            submitButton.style.display = 'none';
            next_questionButton.style.color = 'green';
            next_questionButton.style.border = '2px solid green'; 
            answer.innerText = 'correct';
            description.innerText = "  let's go";
            
        });
    } else {
        console.error("Element with id 'respone_box' not found");
    }
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
            descriptionBox.style.backgroundColor = '#FFDFE0';
            submitButton.style.display = 'none';
            next_questionButton.style.color = 'red';
            next_questionButton.style.border = '2px solid red'; 
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

// Usage





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

    all_list = [choice1,choice2,choice3,choice4];
    all_choice = [incorrect_list[0],incorrect_list[1],incorrect_list[2],answer];

    all_list = shuffleArray(all_list);

    for (let i = 0; i < all_list.length; i++) {
        all_list[i].innerHTML = all_choice[i];
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
    nextQuestionButton.addEventListener('click', function(event) {
        event.preventDefault();
        
        
        displayQuestion(full_object,index);
        index = index + 1;
        console.log(full_object[index].incorrect_list);
        displayChoice(full_object[index].incorrect_list,index,full_object[index].answer);

        
    })
    
    

 
    

    correctAnswer()
    



});

