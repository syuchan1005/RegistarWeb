import axios from 'axios';
import AxiosMockAdapter from 'axios-mock-adapter';

if (process.env.NODE_ENV !== 'production' && false) {
  /* eslint-disable-next-line */
  console.info('%cNow use AxiosMock!', 'color: red;');
  const mock = new AxiosMockAdapter(axios);

  mock.onGet('/api/products/list').reply(200, {
    data: [
      {
        id: 0,
        name: 'TEST',
        price: 150,
      },
      {
        id: 1,
        name: 'test',
        price: 300,
      },
    ],
  });

  mock.onPost('/api/products/add').reply(200, {
    id: 999,
  });

  mock.onPost('/api/products/delete').reply(200, {
    success: true,
  });

  mock.onPost('/api/order/add').reply(200, {
    success: true,
  });

  mock.onPost('/api/order/delete').reply(200, {
    success: true,
  });

  mock.onGet('/api/order/total').reply(200, {
    money: '1500',
    amount: 10,
  });

  mock.onAny().passThrough();
}

export default axios;
