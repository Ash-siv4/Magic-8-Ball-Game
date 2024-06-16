async function shakeBall() {
  const questionInput = document.getElementById("question");
  const responseDiv = document.getElementById("response");

  if (questionInput.value.trim() === "") {
    responseDiv.textContent = "Please ask a question!";
    return;
  }

  const response = await fetch("/shake", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ question: questionInput.value }),
  });

  const data = await response.json();

  if (response.ok) {
    responseDiv.textContent = data.response;
  } else {
    responseDiv.textContent = "Error: " + data.error;
  }
}
