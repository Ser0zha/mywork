package ru.ac.uniyar.testingcourse;

import org.junit.jupiter.api.Nested;
import org.junit.jupiter.api.Test;

import static org.assertj.core.api.Assertions.assertThat;
import static org.assertj.core.api.Assertions.assertThatThrownBy;

public class CourseTest {

    // Тестовые данные
    int student1 = 1;
    int student2 = 2;
    int student3 = 3;
    int student4 = 4;
    int student5 = 5;
    int maxStudents = 3;

    // Вспомогательные методы для создания состояний
    Course createNotFullCourse() {
        Course course = new Course(maxStudents);
        course.enroll(student1);
        return course;
    }

    Course createFullCourse() {
        Course course = new Course(maxStudents);
        course.enroll(student1);
        course.enroll(student2);
        course.enroll(student3);
        return course;
    }

    Course createCourseWithWaitingOne() {
        Course course = new Course(maxStudents);
        course.enroll(student1);
        course.enroll(student2);
        course.enroll(student3);
        course.enroll(student4); // попадает в waiting
        return course;
    }


    // Проверочные методы
    static void assertCourseIsNotFull(Course course) {
        assertThat(course.isFullyEnrolled()).isFalse();
    }

    static void assertCourseIsFull(Course course) {
        assertThat(course.isFullyEnrolled()).isTrue();
        assertThat(course.hasWaitingList()).isFalse();
    }

    static void assertWaitingListIsNotEmpty(Course course) {
        assertThat(course.hasWaitingList()).isTrue();
    }

    @Test
    void constructorShouldThrowForInvalidMaxStudents() {
        assertThatThrownBy(() -> new Course(0))
                .isInstanceOf(IllegalArgumentException.class);
    }

    // Тестовые классы
    @Nested
    class CourseIsNotFullTest {

        Course course = createNotFullCourse();

        /**
         * Действие: enroll(student2)
         * Ожидаемый результат: getEnrollmentList вернет список из [1, 2];
         * Курс остается в состоянии CourseIsNotFull
         */
        @Test
        void enrollShouldAddStudent() {
            course.enroll(student2);
            assertThat(course.getEnrollmentList())
                    .containsExactly(student1, student2);
        }

        /**
         * Действие: enroll(student1)
         * Ожидаемый результат: getEnrollmentList вернет список из [1];
         * Курс остается в состоянии CourseIsNotFull
         */
        @Test
        void enrollShouldDoNotAddEnrolledStudent() {
            course.enroll(student1);
            assertThat(course.getEnrollmentList())
                    .containsExactly(student1);
            assertCourseIsNotFull(course);
        }

        /**
         * Действие: unenroll(student1)
         * Ожидаемый результат: getEnrollmentList вернет пустой список [];
         * Курс остается в  =состоянии CourseIsNotFull
         */

        @Test
        void unenrollShouldRemoveStudent() {
            course.unenroll(student1);
            assertThat(course.getEnrollmentList()).isEmpty();
            assertCourseIsNotFull(course);
        }

        /**
         * Действие: unenroll(student2)
         * Ожидаемый результат: getEnrollmentList вернет список из [1];
         * Курс остается в = состоянии CourseIsNotFull
         */
        @Test
        void unenrollShouldDoNotRemoveUnenrolledStudent() {
            course.unenroll(student2);
            assertThat(course.getEnrollmentList())
                    .containsExactly(student1);
            assertCourseIsNotFull(course);
        }

        /**
         * Действие:
         * enroll(student2)
         * enroll(student3)
         * Ожидаемый результат: объект перейдет в состояние CourseIsFull
         */
        @Test
        void enrollingStudentMakesCourseIsFull(){
            course.enroll(student2);
            course.enroll(student3);
            assertCourseIsFull(course);
        }
    }

    @Nested
    class CourseIsFullTest {
        Course course = createFullCourse();

        /**
         * Действие: enroll(student2)
         * Ожидаемый результат: getEnrollmentList вернет список из [1, 2, 3];
         * Курс остается в состоянии CourseIsFull
         */
        @Test
        void enrollShouldDoNotAddEnrolledStudentInFull() {
            course.enroll(student1);
            assertThat(course.getEnrollmentList())
                    .containsExactly(student1, student2, student3);
            assertCourseIsFull(course);
        }

        /**
         * Действие:unenroll(student4)
         * Ожидаемый результат: getEnrollmentList вернет список из [1, 2, 3];
         * Курс остается в состоянии CourseIsFull
         */
        @Test
        void unenrollIgnoreRemoveUnenrolledStudent(){
            course.unenroll(student4);
            assertThat(course.getEnrollmentList())
                    .containsExactly(student1, student2, student3);
            assertCourseIsFull(course);
        }

        /**
         * Действие:unenroll(student2)
         * Ожидаемый результат: getEnrollmentList вернет список из [1, 3];
         * Курс переходит в состояние CourseIsNotFull
         */
        @Test
        void unenrollRemoveUnenrolledStudent(){
            course.unenroll(student2);
            assertThat(course.getEnrollmentList())
                    .containsExactly(student1, student3);
            assertCourseIsNotFull(course);
        }

        /**
         * Действие:enroll(student4)
         * Ожидаемый результат: getEnrollmentList вернет список из [1, 2, 3];
         * getWaitingList вернет список из [4];
         * Курс переходит в состояние WaitingListIsNotEmpty
         */
        @Test
        void enrollShouldAddToWaitingWhenCourseFull() {
            course.enroll(student4);

            assertThat(course.getWaitingList())
                    .containsExactly(student4);
            assertThat(course.getEnrollmentList())
                    .containsExactly(student1, student2, student3);

            assertWaitingListIsNotEmpty(course);
        }
    }

    @Nested
    class CourseWaitingListIsNotEmptyTest {
        Course course = createCourseWithWaitingOne();

        /**
         * Действие:enroll(student1)
         * Ожидаемый результат: getEnrollmentList вернет список из [1, 2, 3];
         * getWaitingList вернет список из [4];
         * Курс остается в состоянии WaitingListIsNotEmpty
         */
        @Test
        void enrollShouldIgnoreEnrolledStudent() {
            course.enroll(student1);
            assertThat(course.getWaitingList()).containsExactly(student4);
            assertThat(course.getEnrollmentList()).containsExactly(student1, student2, student3);
            assertWaitingListIsNotEmpty(course);
        }

        /**
         * Действие:enroll(student4)
         * Ожидаемый результат: getEnrollmentList вернет список из [1, 2, 3];
         * getWaitingList вернет список из [4];
         * Курс остается в состоянии WaitingListIsNotEmpty
         */
        @Test
        void enrollShouldIgnoreWaitingStudent() {
            course.enroll(student4);
            assertThat(course.getWaitingList()).containsExactly(student4);
            assertThat(course.getEnrollmentList()).containsExactly(student1, student2, student3);
            assertWaitingListIsNotEmpty(course);
        }

        /**
         * Действие:enroll(student5)
         * Ожидаемый результат: getEnrollmentList вернет список из [1, 2, 3];
         * getWaitingList вернет список из [4, 5];
         * Курс остается в состоянии WaitingListIsNotEmpty
         */
        @Test
        void enrollShouldAddNewStudentToWaiting() {
            course.enroll(student5);
            assertThat(course.getWaitingList()).containsExactly(student4, student5);
            assertThat(course.getEnrollmentList()).containsExactly(student1, student2, student3);
            assertWaitingListIsNotEmpty(course);
        }

        /**
         * Действие:unenroll(student5)
         * Ожидаемый результат: getEnrollmentList вернет список из [1, 2, 3];
         * getWaitingList вернет список из [4];
         * Курс остается в состоянии WaitingListIsNotEmpty
         */
        @Test
        void unenrollShouldIgnoreNonExistentStudent() {
            course.unenroll(student5);
            assertThat(course.getWaitingList()).containsExactly(student4);
            assertThat(course.getEnrollmentList()).containsExactly(student1, student2, student3);
            assertWaitingListIsNotEmpty(course);
        }

        /**
         * Действие:enroll(student5)
         * unenroll(student4)
         * Ожидаемый результат: getEnrollmentList вернет список из [1, 2, 3];
         * getWaitingList вернет список из [5];
         * Курс остается в состоянии WaitingListIsNotEmpty
         */
        @Test
        void unenrollShouldRemoveFromMiddleOfWaitingList() {
            course.enroll(student5);
            course.unenroll(student4);
            assertThat(course.getEnrollmentList()).containsExactly(student1, student2, student3);
            assertThat(course.getWaitingList()).containsExactly(student5);
            assertWaitingListIsNotEmpty(course);
        }

        /**
         * Действие:enroll(student5)
         * unenroll(student1)
         * Ожидаемый результат: getEnrollmentList вернет список из [2, 3, 4];
         * getWaitingList вернет список из [5];
         * Курс остается в состоянии WaitingListIsNotEmpty
         */
        @Test
        void unenrollShouldPromoteFirstWaitingWhenMultipleExist() {
            course.enroll(student5);

            course.unenroll(student1);
            assertThat(course.getEnrollmentList()).containsExactly(student2, student3, student4);
            assertThat(course.getWaitingList()).containsExactly(student5);
            assertWaitingListIsNotEmpty(course);
        }

        /**
         * Действие:unenroll(student1)
         * Ожидаемый результат: getEnrollmentList вернет список из [2, 3, 4];
         * getWaitingList вернет список из [];
         * Курс переходит в состояние CourseIsFull
         */
        @Test
        void unenrollShouldPromoteOnlyWaitingStudent() {
            course.unenroll(student1);
            assertThat(course.getEnrollmentList()).containsExactly(student2, student3, student4);
            assertThat(course.getWaitingList()).isEmpty();
            assertCourseIsFull(course);
        }

        /**
         * Действие:unenroll(student4)
         * Ожидаемый результат: getEnrollmentList вернет список из [1, 2, 3];
         * getWaitingList вернет список из [];
         * Курс переходит в состояние CourseIsFull
         */
        @Test
        void unenrollShouldRemoveWaitingStudent() {
            course.unenroll(student4);
            assertThat(course.getWaitingList()).isEmpty();
            assertThat(course.getEnrollmentList()).containsExactly(student1, student2, student3);
            assertCourseIsFull(course);
        }
    }
}