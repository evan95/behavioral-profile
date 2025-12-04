document.getElementById('submit-btn').addEventListener('click', function() {
  const form = document.getElementById('quiz-form');
  const answers = [];
  const qcount = document.querySelectorAll('.question').length;
  for (let i = 1; i <= qcount; i++) {
    const chosen = document.querySelector('input[name="q' + i + '"]:checked');
    if (!chosen) {
      alert('Please answer all questions before submitting.');
      return;
    }
    answers.push(parseInt(chosen.value, 10));
  }
  document.getElementById('answers').value = JSON.stringify(answers);
  form.submit();
});
