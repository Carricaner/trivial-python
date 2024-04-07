import matplotlib.pyplot as plt
import pandas as pd
import pyarrow.parquet as pq


def try_plot() -> None:
    # Sample data
    data = {
        'Year': [2010, 2011, 2012, 2013, 2014],
        'Sales': [1000, 1500, 1200, 1800, 2000]
    }

    # Create a DataFrame from the sample data
    df = pd.DataFrame(data)

    # Plotting using pandas and matplotlib
    df.plot(x='Year', y='Sales', kind='line', marker='o', linestyle='-')

    # Adding labels and title
    plt.xlabel('Year')
    plt.ylabel('Sales')
    plt.title('Sales Over Time')

    # Display the plot
    plt.grid(True)
    plt.show()


if __name__ == '__main__':
    parquet_file = pq.ParquetFile('../../data/example.parquet')
    print(parquet_file.metadata)
    print(pq.read_metadata('../../data/example.parquet'))
    # print(parquet_file.schema)
    # print(parquet_file.num_row_groups)
    # print(parquet_file.read_row_group(0))



