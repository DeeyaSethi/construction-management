// Function to fetch and display real-time inventory data and update the pie chart
function displayInventory() {
    const inventoryTable = document.getElementById("inventory-table");
    const tbody = inventoryTable.querySelector("tbody");
    const pieChartCanvas = document.getElementById("inventory-pie-chart");

    // Dummy inventory data with status flags
    const dummyInventoryData = [
        { productName: "Product 1", quantity: 2, price: 10.99, purchaseDate: "2023-10-01", exhaustionDate: "2023-11-01", status: "sufficient" },
        { productName: "Product 2", quantity: 1, price: 15.49, purchaseDate: "2023-09-01", exhaustionDate: "2023-10-01", status: "running-out-fast" },
        { productName: "Product 3", quantity: 8, price: 5.99, purchaseDate: "2023-10-15", exhaustionDate: "2023-11-30", status: "sufficient" },
        { productName: "Product 4", quantity: 15, price: 12.99, purchaseDate: "2023-09-20", exhaustionDate: "2023-10-20", status: "overstock" },
        { productName: "Product 5", quantity: 0, price: 8.49, purchaseDate: "2023-09-05", exhaustionDate: "2023-09-15", status: "stockout" },
    ];

    tbody.innerHTML = ''; // Clear existing data

    const productQuantities = {};

    dummyInventoryData.forEach((item) => {
        const totalValue = (item.quantity * item.price).toFixed(2);
        const row = document.createElement("tr");
        row.innerHTML = `
            <td>${item.productName}</td>
            <td>${item.quantity}</td>
            <td>${item.price}</td>
            <td>${totalValue}</td>
            <td>${item.purchaseDate}</td>
            <td>${item.exhaustionDate}</td>
            <td class="${item.status}">${item.status}</td>
        `;
        tbody.appendChild(row);

        // Update product quantities for the pie chart
        if (productQuantities[item.productName]) {
            productQuantities[item.productName] += item.quantity;
        } else {
            productQuantities[item.productName] = item.quantity;
        }
    });

    // Create and update the pie chart based on product quantities
    const productLabels = Object.keys(productQuantities);
    const productQuantitiesData = Object.values(productQuantities);

    const pieChart = new Chart(pieChartCanvas, {
        type: 'pie',
        data: {
            labels: productLabels,
            datasets: [{
                data: productQuantitiesData,
                backgroundColor: [
                    'rgba(0, 128, 0, 0.7)',
                    'rgba(255, 165, 0, 0.7)',
                    'rgba(0, 0, 255, 0.7)',
                    'rgba(255, 0, 0, 0.7)',
                    'rgba(128, 0, 128, 0.7)',
                ],
            }],
        },
    });
}

// Function to open the "Add Product" page
function openAddProductPage() {
    // Create a new window or tab for the "Add Product" page
    const addProductPage = window.open("add_product.html", "_blank");
}

// Display the initial inventory data and pie chart
displayInventory();

// Attach event listener to the "Add to Inventory" button
const addProductButton = document.getElementById("add-product-button");
addProductButton.addEventListener("click", openAddProductPage);

// Display the initial inventory data and pie chart
//displayInventory();
