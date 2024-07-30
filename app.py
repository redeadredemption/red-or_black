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
