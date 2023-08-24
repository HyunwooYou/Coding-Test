let _products;
let _purchased;

const solution = (products, purchased) => {
  let priority_map = new Map();
  let pending_list = [];

  // init priority map
  for (let i = 0; i < products.length; i++) {
    const product_infos = products[i].split(' ');

    for (let j = 0; j < product_infos.length; j++) {
      const character = product_infos[j];

      if (priority_map.has(character)) {
        const prev_value = priority_map.get(character);
        priority_map.set(character, prev_value + 1);
      } else {
        priority_map.set(character, 1);
      }
    }
  }

  // init pending list
  for (let i = 0; i < products.length; i++) {
    const product_infos = products[i].split(' ');
    const product_name = product_infos.shift(-1);

    if (purchased.includes(product_name)) {
      continue;
    }

    pending_list.push({
      name: product_name,
      // character name to weight number
      weightsList: product_infos.map((character) =>
        priority_map.get(character),
      ),
    });
  }

  const sorted_priority_array = [...priority_map].sort((a, b) => b[1] - a[1]);

  for (let i = 0; i < sorted_priority_array.length; i++) {
    const weight = sorted_priority_array[i][1];
    const filtered = pending_list.filter((obj) =>
      obj.weightsList.includes(weight),
    );

    if (filtered.length === 0) {
      continue;
    }

    pending_list = filtered;
  }

  return pending_list[0].name;
};

_products = [
  'towel red long thin',
  'pillow red long',
  'mattress thick',

  'blanket red thick short',
  'curtain red long wide',
  'hat red thin',
  'muffler blue thick long',
];
_purchased = ['blanket', 'curtain', 'hat', 'muffler'];

// towel
console.log(solution(_products, _purchased));

_products = [
  'blanket blue long',
  'sofa red long',

  'towel red',
  'mattress long',
  'curtain blue long cheap',
];
_purchased = ['towel', 'mattress', 'curtain'];

// blanket
console.log(solution(_products, _purchased));
