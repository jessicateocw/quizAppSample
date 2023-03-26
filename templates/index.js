const form = document.getElementById("quiz-form");

form.addEventListener("submit", function (event) {
  const questionContainers = document.querySelectorAll(".question");
  let formValid = true;

  for (let i = 0; i < questionContainers.length; i++) {
    const radioButtons = questionContainers[i].querySelectorAll(
      'input[type="radio"]'
    );
    let radioChecked = false;

    for (let j = 0; j < radioButtons.length; j++) {
      if (radioButtons[j].checked) {
        radioChecked = true;
        break;
      }
    }

    if (!radioChecked) {
      questionContainers[i].classList.add("error");
      questionContainers[i].querySelector(".error-message").textContent =
        "Please select an answer.";
      formValid = false;
    } else {
      questionContainers[i].classList.remove("error");
      questionContainers[i].querySelector(".error-message").textContent = "";
    }
  }

  if (!formValid) {
    event.preventDefault();
    document.querySelector(".form-error").textContent =
      "Please answer all questions."; // show error message
    window.scrollTo(0, 0);
  }
});
