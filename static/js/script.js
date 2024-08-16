console.log("Physio Appointment Project Loaded");

document.addEventListener("DOMContentLoaded", function () {
    // Handle Date and Time Slot Selection if elements exist
    const dateInput = document.getElementById("id_date");
    const timeSelect = document.getElementById("id_time");

    if (dateInput && timeSelect) {
        dateInput.addEventListener("change", function () {
            const selectedDate = dateInput.value;
            console.log("Date selected:", selectedDate);

            if (selectedDate) {
                fetch(`/appointments/get_available_time_slots/?date=${selectedDate}`)
                    .then(response => response.json())
                    .then(data => {
                        console.log("Available time slots:", data);

                        // Clear existing options
                        timeSelect.innerHTML = "";

                        // Add new options
                        data.forEach(time => {
                            const option = document.createElement("option");
                            option.value = time;
                            option.textContent = time;
                            timeSelect.appendChild(option);
                        });
                    })
                    .catch(error => {
                        console.error("Error fetching time slots:", error);
                    });
            }
        });
    } else {
        console.warn("Date input or time select element not found. Skipping date/time related functionality.");
    }
});
