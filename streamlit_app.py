import streamlit as st
import asyncio
from query_engine import QueryEngine  # Import your AI-powered search engine

async def search_query(user_query):
    search_engine = QueryEngine()
    results = await search_engine.hybrid_search(user_query)
    return results

def main():
    st.title("🔍 AI-Powered Natural Language Search")

    query = st.text_input("Enter your query:")
    
    if st.button("Search"):
        if query:
            with st.spinner("Processing your query..."):
                results = asyncio.run(search_query(query))

                if results:
                    st.subheader("🔹 Search Results:")
                    
                    # Convert records into a list of dictionaries
                    data = [dict(record) for record in results]
                    
                    if data:
                        st.dataframe(data)  # Display results in a table
                    else:
                        st.warning("No results found!")
                else:
                    st.warning("No results found!")
        else:
            st.warning("Please enter a search query!")

if __name__ == "__main__":
    main()
    
