# Red or Black?

This is a simple Streamlit web application that allows users to vote for their favorite color between Red and Black. The app displays the current vote counts in a bar chart.

## Features

- Users can vote for either Red or Black.
- Each user can vote only once by entering their name.
- Displays the current vote counts in a bar chart.
- Vote counts are stored in the session state.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/redeadredemption/red_or_black.git
   cd red_or_black
   ```

2. Install the required packages:
   ```bash
   pip install streamlit pandas matplotlib
   ```

## Usage

1. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

2. Open your web browser and go to `http://localhost:8501` to access the app.

## Code Overview

The main functionality of the app is implemented in `app.py`:

```python
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Initialize session state for votes
if 'votes' not in st.session_state:
    st.session_state.votes = {'Red': 0, 'Black': 0}
    st.session_state.names = []

st.title('Red or Black?')

name = st.text_input('Enter your name:')
color = st.radio('Vote for your favorite color:', ['Red', 'Black'])
submit = st.button('Submit Vote')

if submit:
    if name in st.session_state.names:
        st.warning('You have already voted!')
    elif name.strip() == '':
        st.warning('Please enter a valid name.')
    else:
        st.session_state.names.append(name)
        st.session_state.votes[color] += 1
        st.success(f'Thank you for voting, {name}!')

# Display the bar chart with custom colors
votes_df = pd.DataFrame(list(st.session_state.votes.items()), columns=['Color', 'Votes'])
fig, ax = plt.subplots()
colors = ['#FF0000' if color == 'Red' else '#000000' for color in votes_df['Color']]
bars = ax.bar(votes_df['Color'], votes_df['Votes'], color=colors)

plt.xticks(rotation=0)
plt.xlabel('Color')
plt.ylabel('Votes')
plt.ylim(0, max(votes_df['Votes']) + 1)
st.pyplot(fig)

# Display the current vote counts
st.write('Current vote counts:')
st.write(votes_df)
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request with any improvements or bug fixes.

## License

This project is licensed under the MIT License.
