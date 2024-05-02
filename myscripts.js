fetch('./question.json')
    .then((response) => response.json())
    .then((json) => {
        questions = json.questions;
        let currentQuestionIndex = 0;
        const scoreElement = document.getElementById('Score');
        let score = 0;
        scoreElement.innerHTML = 'Current Score: ' + score;

        function getQuestion() {
            const question = questions[currentQuestionIndex];
            return question;
        }

        function getAnswer() {
            const answers = questions[currentQuestionIndex].answers;
            return answers;
        }

        function displayQuestion() {
            const questionElement = document.getElementById('Question');
            questionElement.innerHTML = getQuestion().question;
            // get the question and answers
            const choices = ['choice1', 'choice2', 'choice3', 'choice4'];
            const values = ['value1', 'value2', 'value3', 'value4'];
            const randomChoice = Math.floor(Math.random() * choices.length);
            // set the answer
            // console.log(getAnswer());
            const answer = getAnswer();
            document.getElementById(choices[randomChoice]).innerHTML = answer;
            const answerPosition = choices.indexOf(choices[randomChoice]);
            document.getElementById(values[answerPosition]).value = answer;
            choices.splice(answerPosition, 1);
            values.splice(answerPosition, 1);

            let wrongList = getQuestion().wrong;
            for (let i = 0; i < choices.length; i++) {
                let wrongChoice = wrongList[i];
                document.getElementById(choices[i]).innerHTML = wrongChoice;
                document.getElementById(values[i]).value = wrongChoice;
            }
        }

        function handleSubmit(event) {
            event.preventDefault();
            const selectedChoice = document.querySelector('input[name="choice"]:checked').value;
            if (selectedChoice === getAnswer()) {
                score++;
                scoreElement.innerHTML = 'Current Score: ' + score;
            }

            currentQuestionIndex++;
            if (currentQuestionIndex < questions.length) {
                displayQuestion();
            } else {
                alert('Game over! Your score is ' + score);
            }
        }

        displayQuestion();

        const form = document.querySelector('form');
        form.addEventListener('submit', handleSubmit);
    });