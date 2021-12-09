function createChart(name, labels, data) {
    let ctx = document.getElementById(name).getContext("2d");
    return new Chart(ctx, {
        type: "bar",
        data: {
            labels: labels,
            datasets: [
                {
                    label: "Cantidad de Quarterbacks",
                    data: data,
                    backgroundColor: ["rgba(0, 123, 255, 0.2)"],
                    borderColor: ["rgba(0, 123, 255, 1)"],
                    borderWidth: 1,
                },
            ],
        },
        options: {
            scales: {
                y: {
                    beginAtZero: true,
                },
            },
        },
    });
}
