document.querySelectorAll('input[name="rating"]').forEach((radio) => {
    radio.addEventListener('change', () => {
      const rating = document.querySelector('input[name="rating"]:checked').value;
      alert(`Você deu uma nota de ${rating} estrelas!`);
    });
  });
  