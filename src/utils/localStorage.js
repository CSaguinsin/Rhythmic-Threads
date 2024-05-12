const getItem = (key) => {
  try {
    return JSON.parse(localStorage.getItem(key));
  } catch (error) {
    console.error("Error getting item from local storage", error);
    return null;
  }
};

const setItem = (key, value) => {
  try {
    localStorage.setItem(key, JSON.stringify(value));
  } catch (error) {
    console.error("Error setting item in local storage", error);
  }
};

const removeItem = (key) => {
  try {
    localStorage.removeItem(key);
  } catch (error) {
    console.error("Error removing item from local storage", error);
  }
};

// remove all items from local storage
const clear = () => {
  try {
    localStorage.clear();
  } catch (error) {
    console.error("Error clearing local storage", error);
  }
};

export default { getItem, setItem, removeItem, clear };
