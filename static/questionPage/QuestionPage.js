// var incorrectData = JSON.parse('{{ incorrect}}');
// console.log(incorrectData);


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
document.addEventListener('DOMContentLoaded', function() {
    const nextQuestionButton = document.getElementById('next_question');
    
    if (nextQuestionButton) {
        nextQuestionButton.addEventListener('click', function(event) {
            // Reload the page when the "Next Question" button is clicked
            location.reload();// reload the page rn, but gonna be next question no reload
        });
    }
});
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
    


document.addEventListener('DOMContentLoaded', correctAnswer);