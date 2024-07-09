
#------------------ Getting names for a csv too big to open -----------------------------------------
# Read the first line to get the column names
with open(file_path, 'r', encoding='utf-8') as file:
    header_line = file.readline().strip()

# Split the header line to get the column names
column_names = header_line.split('\t')
print(column_names)

#-------------- Chunk Inserting into Duck DB----------------------------------------------------
# Function to insert a DataFrame chunk into DuckDB
chunk_size = 10000
def insert_chunk(con, df_chunk):
    try:
        con.execute("INSERT INTO my_table SELECT * FROM df_chunk")
    except Exception as e:
        print(f"Error inserting chunk: {e}")

# Read the TSV file in chunks
for chunk in pd.read_csv(file_path, sep='\t', chunksize=chunk_size, iterator=True):
    # Ensure the chunk uses the correct column names
    if len(chunk.columns) == len(column_names):
        chunk.columns = column_names
        dbcon.register('df_chunk', chunk)  # Register the chunk as a temporary view in DuckDB
        insert_chunk(dbcon, chunk)
    else:
        print(f"Skipping chunk with {len(chunk.columns)} columns instead of {len(column_names)}")

# Query the data to verify it has been loaded correctly
result = dbcon.execute("SELECT * FROM my_table limit 10").fetchdf()