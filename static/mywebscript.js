const getValue = (id) => document.getElementById(id).value;

const displayResult = (message) => {
    document.getElementById("system_response").innerText = message;
};

const runOperation = async (operation) => {
    const num1 = getValue("num1");
    const num2 = getValue("num2");

    if (!num1 || !num2) {
        return displayResult("Please enter both numbers.");
    }

    try {
        const res = await fetch(`/${operation}?num1=${num1}&num2=${num2}`);
        const data = await res.text();
        displayResult(`Result: ${data}`);
    } catch (err) {
        displayResult("Server error. Please try again.");
    }
};

const runSingleInput = async (operation) => {
    const num = getValue("num1");

    if (!num) {
        return displayResult("Please enter Number 1 for this operation.");
    }

    try {
        const res = await fetch(`/${operation}?num=${num}`);
        const data = await res.text();
        displayResult(`Result: ${data}`);
    } catch (err) {
        displayResult("Server error. Please try again.");
    }
};

 