program kadai
    implicit none
    integer :: num, wid, n
    integer, allocatable :: list(:)
    real(8), allocatable :: cen(:)
    integer, allocatable :: lhist(:)

    read(*,*) num
    allocate(list(num))
    read(*,*) list
    read(*,*) wid

    !widが100の約数であることを想定
    n = 100 / wid
    allocate(cen(n))
    allocate(lhist(n))

    call histogram(list, wid, cen, lhist)
    stop
    contains
    subroutine histogram(score, binw, binc, hist)
        implicit none
        integer, intent(in) :: score(:)
        integer, intent(in) :: binw
        real(8), intent(out) :: binc(:)
        integer, intent(out) :: hist(:)

        integer :: i, j
        real(8) :: rbinw

        rbinw = dble(binw)

        do i = 1, n
            hist(i) = 0
        end do
        do i = 1, num
            j = score(i) / binw + 1
            if (j < 1 .or. j > n) then
                write(*,*) 'Errer'
                stop
            else
                hist(j) = hist(j) + 1
            end if
        end do
        do i = 1, n
            if (i == 1) then
                binc(1) = rbinw / 2.0
            else
                binc(i) = binc(i - 1) + rbinw
            end if
        end do

        do i = 1, n
            write(*,*) binc(i), hist(i)
        end do
    end subroutine
end program kadai