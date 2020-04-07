Sales Data Analyzer is a plain text file parser and data analyser, and a report generator system. It imports flat files, parses data from each file, analyses its data and generates a report output file for each input file.

The following sections describe the input file reader, the expected data format of the input files, the data analysis performed and the generated output report file.

## Input File Reader
The application reads every new file with the ```.dat``` extension in ```$HOME/data/in/``` path. Each file is parsed, according to an expected formatting layout, and its data is analyzed.

## Input File Data
There are three possible types of data for each line, each with a specific format:
1. _salesman_
2. _customer_
3. _sales_

Any lines containing invalid formatted data are ignored.

### 1. Salesman Data Format
A _salesman_ data line starts with a 3-character id ```001``` and has the following layout:

```001ç<cpf>ç<name>ç<salary>```

Fields constraints:
- _cpf_: a 11 character-wide numeric only field;
- _name_: can contain any characters except ```'ç'```; must have length ≥ 1;
- _salary_: can contain any digit in [0-9] and at most one ```'.'``` character; must have length ≥ 1;

### 2. Customer Data Format
A _customer_ data line starts with a 3-character id ```002``` and has the following layout:

```002ç<cnpj>ç<name>ç<business_area>```

Fields constraints:
- _cnpj_: a 14 character-wide numeric only field;
- _name_: can contain any characters except ```'ç'```; must have length ≥ 1;
- _business_area_: can contain any characters except ```'ç'```; must have length ≥ 1;

### 3. Sales Data Format
A _sales_ data line starts with a 3-character id ```003``` and has the following layout:

```003ç<sale_id>ç<item_list>ç<salesman_name>```

Fields constraints:
- _sale_id_: can contain any digit in [0-9]; must have length ≥ 1;
- _item_list_: a comma-separated list, containing at least one _item_, with the following layout:
    
    ```[<item_id_1>-<item_quantity_1>-<item_price_1>,<item_id_2>-<item_quantity_2>-<item_price_2>,...,<item_id_n>-<item_quantity_n>-<item_price_n>]```
    
    Fields constraints:
    - _item_id_: can contain any digit in [0-9]; must have length ≥ 1;
    - _item_quantity_: can contain any digit in [0-9]; must have length ≥ 1;
    - _item_price_: can contain any digit in [0-9] and at most one ```'.'``` character; must have length ≥ 1;

- _salesman_name_: can contain any characters except ```'ç'```; must have length ≥ 1;

## Data Analysis
The application summarizes for each input file the following data:
- _amount of clients_ in the input file;
- _amount of salesman_ in the input file;
- id of the _most expensive sale_ in the input file;
- _worst salesman_ ever in the input file;

## Output File Generator
An output report file named ```<input_file_name>.done.dat``` is created in ```$HOME/data/out/``` path for each input file analysed.

### Report Data Format
The output report file has the following layout:

```
amount of clients: <clients_num>
amount of salesman: <salesman_num>
most expensive sale: <sale_id>
worst salesman ever: <salesman_name>
```
