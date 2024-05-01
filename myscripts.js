
fetch('./question.json')
    .then((response) => response.json())
    .then((json) =>  {
        questions = json.questions;
        //console.log(questions[0].question);
        const randomNumber = Math.floor(Math.random() * questions.length);
        function getQuestion(questions,randomNumber) {
    
            
            const question = questions[randomNumber];
        
            return question;
            
        }
        function getAnswer(question,randomNumber) {

            const answers = question[randomNumber];

            return answers;



        }
        console.log(getAnswer)
        document.getElementById('Question').innerHTML = getQuestion(questions,randomNumber).question;
        document.getElementById('choice2').innerHTML = getAnswer( questions,randomNumber).answers;
        
    });



// add the question to the id Question
