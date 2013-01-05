from conway import *
import unittest


class Test(unittest.TestCase):
    def test_live_cell_with_no_neighbours_dies(self):
        cell_alive = evolve_cell(alive=True, neighbours=0)
        self.assertFalse(cell_alive)

    def test_live_cell_with_two_neighbours_lives_on(self):
        cell_alive = evolve_cell(alive=True, neighbours=2)
        self.assertTrue(cell_alive)

    def test_live_cell_with_three_neighbours_lives_on(self):
        cell_alive = evolve_cell(alive=True, neighbours=3)
        self.assertTrue(cell_alive)

    def test_live_cell_with_four_neighbours_dies(self):
        cell_alive = evolve_cell(alive=True, neighbours=4)
        self.assertFalse(cell_alive)

    def test_dead_cell_with_three_neighbours_is_born(self):
        cell_alive = evolve_cell(alive=False, neighbours=3)
        self.assertTrue(cell_alive)

    def test_dead_cell_with_two_neighbours_stays_dead(self):
        cell_alive = evolve_cell(alive=False, neighbours=2)
        self.assertFalse(cell_alive)

    def test_dead_cell_with_four_neighbours_stays_dead(self):
        cell_alive = evolve_cell(alive=False, neighbours=4)
        self.assertFalse(cell_alive)

    def test_neighbour_count_of_empty_3x3_grid_is_0(self):
        grid =  [[0, 0, 0],
                 [0, 0, 0],
                 [0, 0, 0]]
        position = (1, 1)
        neighbour_count = count_neighbours(grid, position)
        self.assertEqual(neighbour_count, 0)

    def test_neighbour_count_of_0_middle_3x3_grid_is_correct(self):
        grid =  [[1, 0, 1],
                 [0, 0, 0],
                 [1, 0, 1]]
        position = (1, 1)
        neighbour_count = count_neighbours(grid, position)
        self.assertEqual(neighbour_count, 4)

    def test_neighbour_count_of_1_middle_3x3_grid_is_correct(self):
        grid =  [[1, 0, 1],
                 [1, 1, 1],
                 [1, 0, 1]]
        position = (1, 1)
        neighbour_count = count_neighbours(grid, position)
        self.assertEqual(neighbour_count, 6)

    def test_neighbour_count_of_edge_cell_in_3x3_grid_is_correct(self):
        grid =  [[1, 0, 1],
                 [1, 1, 1],
                 [1, 0, 1]]
        position = (0, 0)
        neighbour_count = count_neighbours(grid, position)
        self.assertEqual(neighbour_count, 2)

    def test_neighbour_count_of_far_edge_cell_in_3x3_grid_is_correct(self):
        grid =  [[1, 0, 1],
                 [1, 1, 1],
                 [1, 0, 1]]
        position = (2, 2)
        neighbour_count = count_neighbours(grid, position)
        self.assertEqual(neighbour_count, 2)

    def test_neighbour_count_of_other_edge_cell_in_3x3_grid_is_correct(self):
        grid =  [[1, 0, 1],
                 [1, 1, 1],
                 [1, 0, 1]]
        position = (2, 1)
        neighbour_count = count_neighbours(grid, position)
        self.assertEqual(neighbour_count, 5)

    def test_neighbour_count_of_1_middle_5x5_grid_is_correct(self):
        grid =  [[1, 0, 1, 0, 1],
                 [0, 1, 0, 1, 0],
                 [1, 0, 1, 0, 1],
                 [0, 1, 0, 1, 0],
                 [1, 0, 1, 0, 1]]
        position = (2, 2)
        neighbour_count = count_neighbours(grid, position)
        self.assertEqual(neighbour_count, 4)

    def test_evolve_empty_3x3_grid_is_correct(self):
        old_grid =  [[0, 0, 0],
                     [0, 0, 0],
                     [0, 0, 0]]

        new_grid =  [[0, 0, 0],
                     [0, 0, 0],
                     [0, 0, 0]]
        self.assertEqual(evolve(old_grid), new_grid)

    def test_evolve_non_empty_3x3_grid_is_correct(self):
        old_grid =  [[1, 0, 1],
                     [0, 1, 1],
                     [0, 1, 1]]

        new_grid =  [[0, 0, 1],
                     [1, 0, 0],
                     [0, 1, 1]]
        evolved = evolve(old_grid)
        print evolved
        print '...', new_grid
        self.assertEqual(evolved, new_grid)

if __name__ == '__main__':
    unittest.main()