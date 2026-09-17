const form = document.getElementById('item-form');

form.addEventListener('submit', async function(e) {
    e.preventDefault();
    // Handle form submission logic here
});

async function fetchData() {
    let tbody = document.querySelector('tbody');

    try {
        const response = await fetch('http://localhost:3000/items');
        const data = await response.json();
        if (data) {
            for (const item of data) {
                const row = document.createElement('tr');
                row.innerHTML = `
                    <td>${item.id}</td>
                    <td>${item.name}</td>
                    <td>${item.price}</td>
                `;
                tbody.appendChild(row);
            }
        } else {
            console.log(data);
        }

        return null;
    } catch {}
}

async function handleDelete(id) {
    try {
        await fetch(`http://localhost:3000/items/${id}`, {
            method: 'DELETE',
        });

        // Optionally, you can remove the deleted item from the DOM or refresh the list
    } catch (error) {

    }
}