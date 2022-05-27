function deleteCalorie(calorieId) {
  fetch("/delete-calories", {
    method: "POST",
    body: JSON.stringify({ calorieId: calorieId }),
  }).then((_res) => {
    window.location.href = "/";
  });
}
