import streamlit as st
import sqlite3
import pandas as pd

# ===================================================================
# DATABASE FUNCTIONS
# ===================================================================

# Function to create the users table if it doesn't exist
def create_table():
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, email TEXT, age INTEGER)')
    conn.commit()
    conn.close()

# Function to add a new user to the database
def add_user(name, email, age):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('INSERT INTO users(name, email, age) VALUES (?, ?, ?)', (name, email, age))
    conn.commit()
    conn.close()

# Function to retrieve all users from the database
def view_users():
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('SELECT * FROM users')
    data = c.fetchall()
    conn.close()
    return data

# Function to delete a user by their ID
def delete_user(user_id):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('DELETE FROM users WHERE id=?', (user_id,))
    conn.commit()
    conn.close()

# ===================================================================
# STREAMLIT UI
# ===================================================================

def main():
    st.title("User Management App")

    menu = ["Add User", "View Users", "Delete User"]
    choice = st.sidebar.selectbox("Menu", menu)

    # --- Added Name for Submission ---
    st.sidebar.markdown("---")
    st.sidebar.info("Created by: Randall Abunan") # <-- CHANGE THIS TO YOUR NAME

    # This function runs first to make sure the database and table are ready
    create_table()


    # This function runs first to make sure the database and table are ready
    create_table()

    # --- Add User Section ---
    if choice == "Add User":
        st.subheader("Add New User")

        name = st.text_input("Name")
        email = st.text_input("Email")
        age = st.number_input("Age", min_value=0, max_value=120)

        if st.button("Submit"):
            add_user(name, email, age)
            st.success(f"User '{name}' added successfully!")

    # --- View Users Section ---
    elif choice == "View Users":
        st.subheader("View All Users")
        
        users = view_users()
        df = pd.DataFrame(users, columns=["ID", "Name", "Email", "Age"])
        st.dataframe(df)

    # --- Delete User Section ---
    elif choice == "Delete User":
        st.subheader("Delete a User")
        
        users = view_users()
        df = pd.DataFrame(users, columns=["ID", "Name", "Email", "Age"])
        st.dataframe(df)

        user_id = st.number_input("Enter ID to delete", min_value=1, step=1)
        
        if st.button("Delete"):
            delete_user(user_id)
            st.warning(f"User with ID {user_id} deleted!")
            # Rerun the app to refresh the user list immediately
            st.rerun()

# This is the standard way to run the main function in a Python script
if __name__ == '__main__':
    main()