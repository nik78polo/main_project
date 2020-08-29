async function Test() {
    const loadingIndicator = document.getElementById('loading-indicator');
    const companyId = document.getElementById("ID").value;

    try {
      const table = document.getElementById('Test1');

      loadingIndicator.innerText = "loading...";
      const list = await getCompanyInfo(companyId);
      console.log(list);

      list.forEach(listItem => {
        table.appendChild(makeRow(listItem));
      });
    } catch (error) {
      console.log(error);
    }

    loadingIndicator.innerText = "";
  }

  async function getCompanyInfo(companyId) {
    const url = 'http://127.0.0.1:8000/api/company/'+companyId;
    const response = await fetch(url);

    if (!response.ok) {
      throw new Error(response.statusText);
    }

    return await response.json();
  }

  function makeRow(listItem) {
    const name = listItem.name;
    const logoSrc= listItem.image;
    const currency = listItem.currency;
    const price = `${listItem.price} ${currency}`;
    const biggestPriceLastYear = `${listItem.biggest_price_last_year} ${currency}`;
    const biggestPriceLastMonth = `${listItem.biggest_price_last_month} ${currency}`;
    const bookValue = listItem.book_value;
    const difference = listItem.difference;

    const tableRow = document.createElement('tr');
    tableRow.className = "table-row";

    tableRow.appendChild(makeNameColumnCell(name, logoSrc));
    tableRow.appendChild(makePriceColumnCell(price));
    tableRow.appendChild(makePriceColumnCell(biggestPriceLastYear));
    tableRow.appendChild(makePriceColumnCell(biggestPriceLastMonth));
    tableRow.appendChild(makePriceColumnCell(bookValue));
    tableRow.appendChild(makeDifferenceCell(difference));

    return tableRow;
  }

  function makeNameColumnCell(name, logoSrc) {
    const tableCell = document.createElement('td');
    const img = document.createElement('img');
    const text = document.createElement('span');

    img.className='test';
    img.setAttribute('src', logoSrc);
    text.innerText = name;
    tableCell.appendChild(img);
    tableCell.appendChild(text);

    return tableCell;
  }

  function makePriceColumnCell(price) {
    const tableCell = document.createElement('td');
    const text = document.createTextNode(price);
    tableCell.appendChild(text);

    return tableCell
  }

  function makeDifferenceCell(difference) {
    let cell = makePriceColumnCell(difference);
    cell.prepend(getTrendingArrow(difference));
    return cell;
  }

  function getTrendingArrow(value) {
    //<span class="material-icons trending-down">trending_down</span>
    const span = document.createElement('span');
    span.className = 'material-icons';

    if (value > 0) {
      span.classList.add('trending-up');
      span.innerText = 'trending_up';
    } else {
      span.classList.add('trending-down');
      span.innerText = 'trending_down';
    }

    return span;
  }