import taskBlock from './taskBlock';

test('taskBlock returns correct values', () => {
  const result = taskBlock(true);
  expect(result).toEqual([false, true]);
});
